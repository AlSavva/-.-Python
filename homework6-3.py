# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут
# должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position
# (должность) на базе класса Worker. В классе Position реализовать методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать
# экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):


    def get_full_name(self):
        return str(self.name + " " + self.surname)

    def get_total_income(self):
        return sum([self._income[i] for i in self._income])


worker1 = Position('Ivan', 'Petrov', 'Manager', 150000, 20000)
print(worker1.get_full_name())
print(worker1.get_total_income())
print(worker1._income, worker1.position)
worker2 = Position('John', 'Petroff', 'Big boss', 450000, 150000)
print(worker2.get_full_name())
print(worker2.get_total_income())
print(worker2._income, worker2.position)
