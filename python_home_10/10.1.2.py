"""Задача № 1.2"""


# Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ

# по заданию №4 урока №7:
# через класс:

class NonNegative:
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Значение скорости не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Car:
    speed = NonNegative()

    def __init__(self, speed, color, name, is_police):
        if speed < 0:
            raise ValueError("Значение скорости не может быть отрицательным")
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
c.speed = -60
print(c.show_speed())

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

