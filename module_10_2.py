import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.counter = 0

    def fight(self, name):
        enemy = 100
        while enemy > 0:
            enemy -= self.power
            self.counter += 1
            print(f'{name}, сражается {self.counter} день(дня)..., осталось {enemy} войнов', end='\n')
            time.sleep(1)

    def run(self):
        print(f'{self.name}, на нас напали')
        self.fight(self.name)
        print(f'{self.name}, одержал победу спустя {self.counter} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
