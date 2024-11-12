import time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            word = f"Какое-то слово № {i}"
            file.write(word + '\n')
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


start = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end = time.time()
print(f'Работа потоков {end - start}')

start = time.time()

threads = []
for word_count, file_name in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
    thread = Thread(target=write_words, args=(word_count, file_name))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end = time.time()
print(f'Работа потоков {end - start}')
