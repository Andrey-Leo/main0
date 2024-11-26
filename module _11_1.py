import requests

# Отправляем GET-запрос на указанный URL
response = requests.get('https://example.com')

# Выводим содержимое ответа на экран
print(response.text)

import pandas as pd

# Читаем данные из файла
df = pd.read_csv('my_file.csv')

# Выводим первые 5 строк данных
print(df.head())

# Выводим информацию о данных
print(df.info())

# Выводим статистические данные о данных
print(df.describe())

import numpy as np

# Создаем массив чисел
arr = np.array([1, 2, 3, 4, 5])

# Выполняем математические операции с массивом
squared_arr = np.square(arr)
sum_arr = np.sum(arr)

# Выводим результаты на экран
print('Квадраты чисел:', squared_arr)
print('Сумма чисел:', sum_arr)

import matplotlib.pyplot as plt

# Создаем данные для графика
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

# Создаем график
plt.plot(x, y)

# Добавляем заголовок и подписи осей
plt.title('Пример графика')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')

# Отображаем график
plt.show()

from PIL import Image

# Открываем изображение
img = Image.open('my_image.jpg')

# Изменяем размер изображения
resized_img = img.resize((200, 200))

# Применяем эффект на изображение
grayscale_img = resized_img.convert('L')

# Сохраняем изображение в другом формате
grayscale_img.save('my_image_gray.jpg', 'JPEG')
