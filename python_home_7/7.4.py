"""Задача №4"""


# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
# к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    @staticmethod
    def go():
         print("машина поехала")

    @staticmethod
    def stop():
        print("машина остановилась")

    @staticmethod
    def turn_direction(direction):
        print(f"машина повернула {direction}")

    def show_speed(self):
        return f"текущая скорость автомобиля: {self.speed}km/h"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"текущая скорость превышена!"
        else:
            return f"текущая скорость автомобиля: {self.speed}km/h"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police, age):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"текущая скорость превышена!"
        else:
            return f"текущая скорость автомобиля: {self.speed}km/h"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, age):
        super().__init__(speed, color, name, is_police)


c = Car(50, 'red', 'lada', False)
print(c.speed, c.color, c.name, c.is_police)
tc = TownCar(80, 'green', 'touota', False)
print(tc.speed, tc.color, tc.name, tc.is_police)
sc = SportCar(100, 'orange', 'bmw', False, 3)
print(sc.speed, sc.color, sc.name, sc.is_police)
wkc = WorkCar(60, 'black', 'lada',  False)
print(wkc.speed, wkc.color, wkc.name, wkc.is_police)
pc = PoliceCar(50, 'blue', 'жигуль', True, 10)
print(pc.speed, pc.color, pc.name, pc.is_police)

lst = [c, tc, sc, wkc, pc]
for el in lst:
    print(el.show_speed())

print('\n')
test_drive = SportCar(140, 'black', 'bmw', False, 5)
print(test_drive.speed, test_drive.color, test_drive.name, test_drive.is_police)
test_drive.go()
test_drive.turn_direction('left')
test_drive.stop()

