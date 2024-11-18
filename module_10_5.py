import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()
            if not line:
                break


filenames = [f'.../module_10/Files/file {number}.txt' for number in range(1, 5)]

# линейный
start_time = time.time()
for name in filenames:
    read_info(name)
end_time = time.time()
print(f'{end_time - start_time} (линейный)')

# многопроцессный
if __name__ == '__main__':

    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f'{end_time - start_time} (многопроцессный)')
