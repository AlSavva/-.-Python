# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем
# атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
# “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil
# (карандаш), Handle (маркер). В каждом из классов реализовать переопределение
# метода draw. Для каждого из классов методы должен выводить уникальное
# сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.
class Stationery:
    title = 'No-name'

    def draw(self):
        print(F'Drow start! {self.title}, line width is not defined.')


class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        print(f'Drow start! {self.title}, line width 3px.')


class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        print(f'Drow start! {self.title}, line width 5px.')


class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        print(f'Drow start! {self.title}, line width 15px.')


other = Stationery()
other.draw()
a = Pen()
b = Pencil()
c = Handle()
print(other.title, a.title, b.title, c.title)
a.draw()
b.draw()
c.draw()
