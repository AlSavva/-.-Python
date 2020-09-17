# Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
# WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который
# должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
# к атрибутам, выведите результат. Выполните вызов методов и также покажите
# результат.
class Car:
    color = 'Unknown'
    name = 'Unknown'
    speed = 60
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def my_car_go(self):
        self.speed = 20
        print(f'Car {self.name} is in motion! BBBDROOM!')

    def my_car_drive(self, speed):
        self.speed = speed
        print(f'Car {self.name} drives at a speed of {self.speed} '
              f'km/h. VROOM! VROOOM!')

    def show_speed(self):
        print(f'Current {self.name} speed is {self.speed} km/h.')

    def my_car_stop(self):
        self.speed = 0
        print(f'Car {self.name} stopped!')

    def my_car_turn(self, direction=None):
        from random import randint
        if self.speed != 0:
            if not direction:
                direct = ['left', 'right', 'back']
                self.direction = direct[randint(1, 3) - 1]
            else:
                self.direction = direction
            print(f'Car {self.name} turn {self.direction}!')
        else:
            print(f'Car {self.name} not drive! Impossible turn!')


class TownCar(Car):

    def show_speed(self):
        if self.speed <= TownCar.speed:
            print(f'Current {self.name} speed is {self.speed} km/h.')
        else:
            print(f'Attention! {self.name} exceeded the speed limit! \nYour '
                  f'speed is {self.speed} km/h.'
                  f'\nSpeed limit is {TownCar.speed} km/h.'
                  f'\nYou exceeded the speed limit by {self.speed - TownCar.speed} '
                  f'km / h')


class SportCar(Car):
    speed = 450
    is_police = False


class PoliceCar(Car):
    speed = 80
    is_police = True


class WorkCar(Car):
    speed = 50
    is_police = False

    def show_speed(self):
        if self.speed <= 40:
            print(f'Current {self.name} speed is {self.speed} km/h.')
        else:
            print(f'Attention! {self.name} exceeded the speed limit! \nYour '
                  f'speed is {self.speed} km/h.'
                  f'\nSpeed limit is 40 km/h.'
                  f'\nYou exceeded the speed limit by {self.speed - 40} '
                  f'km / h')


a = Car('red', 'Tarantas')
a.my_car_go()
print(Car.name, a.name, a.is_police)
a.show_speed()
a.my_car_drive(75)
a.show_speed()
a.my_car_stop()
a.show_speed()
a.my_car_turn()
b = TownCar('green', 'Mazda')
print(b.name, b.speed, b.is_police)
b.my_car_go()
b.my_car_turn()
b.my_car_drive(59)
b.show_speed()
b.my_car_drive(75)
b.show_speed()
b.my_car_stop()
b.show_speed()
print(TownCar.speed, b.speed, b.is_police)
c = SportCar('DeepRed', 'ZAZ')
print(c.name, c.speed, c.is_police)
d = WorkCar('Orange', 'KAMAZ')
print(d.name, d.speed, d.is_police)
d.my_car_go()
d.my_car_turn()
d.my_car_drive(59)
d.show_speed()
d.my_car_drive(75)
d.show_speed()
d.my_car_stop()
d.show_speed()
print(TownCar.speed, b.speed, b.is_police)
e = PoliceCar('white-blue', 'Ford')
print(e.name, e.speed, e.is_police)
