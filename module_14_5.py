from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import crud_functions
from crud_functions import *
import asyncio

api = '7787351381:AAGe4dCdYg5rNLtwy2x4mSuRiHShOVEn6jU'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_in = InlineKeyboardMarkup()
but_in1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
but_in2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_in.add(but_in1, but_in2)

kb_im = InlineKeyboardMarkup()
but_im1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
but_im2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
but_im3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
but_im4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb_im.add(but_im1, but_im2, but_im3, but_im4)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
button4 = KeyboardButton(text='Регистрация')
kb.add(button1, button2)
kb.add(button3)
kb.add(button4)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


class RegistrationState(StatesGroup, State):
    username = State()
    email = State()
    password = State()
    age = State()
    balance = 1000


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if crud_functions.is_included(message.text) is True:
        await  message.answer('Пользователь существует, введите другое имя')
    else:
        async with state.proxy() as data:
            data['username'] = message.text
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    async with state.proxy() as data:
        data['email'] = message.text
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    async with state.proxy() as data:
        data['age'] = message.text
    add_user(data['username'], data['email'], data['age'])
    await message.answer('Регистрация прошла успешно!')
    await state.finish()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_in)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in get_all_products():
        number = i[0]
        title = i[1]
        description = i[2]
        price = i[3]
        with open(f'png{number}.png', 'rb') as img:
            await message.answer_photo(img, f'Название: {title} | '
                                            f'Описание: {description} | '
                                            f'Цена: {price}')
    await message.answer('Выберите продукт для покупки: ', reply_markup=kb_im)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer(text='Вы успешно приобрели продукт!')
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await bot.send_message(call.message.chat.id, 'Норма калорий = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(г) + 5')
    await call.answer()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(user_age=message.text)
    await message.answer('Введите свой рост')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(user_growth=message.text)
    await message.answer('Введите свой вес')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(user_weight=message.text)
    data = await state.get_data()
    calories = 10 * int(data['user_weight']) + 6.25 * int(data['user_growth']) - 5 * int(data['user_age']) + 5
    await message.answer(f'Ваша норма калорий  {calories}')
    await state.finish()


@dp.message_handler()
async def all_massages(message):
    await  message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
