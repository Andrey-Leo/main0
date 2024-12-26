from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_in = InlineKeyboardMarkup()
but_in1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
but_in2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_in.add(but_in1, but_in2)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.add(button1, button2)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_in)


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
