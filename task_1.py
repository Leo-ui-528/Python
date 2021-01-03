import time


class TrafficLight:
    __color = 'red'

    def running(self):
        print(chr(33))

        self.__color = 'red'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(7)

        self.__color = 'yellow'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(2)

        self.__color = 'green'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(1)

        while True:
            self.running()


tr_light = TrafficLight()
print(tr_light.running())