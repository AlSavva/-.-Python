# Реализовать класс Road (дорога), в котором определить атрибуты: length
# (длина), width (ширина). Значения данных атрибутов должны передаваться при
# создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    def __init__(self, lenght, width):
        """length=length in meters, width=width in meters """
        self._lenght = lenght
        self._width = width

    def asf_mas(self, mas_for_sm, thickness):
        """'mas_for_sm'-> asphalt consumption per square meter with a layer
        thickness of 1 centimeter in kg, 'thickness'-> thickness of the layer
        in centimeters.

        return weight of asphalt in tons"""
        return round(
            ((self._lenght * self._width * mas_for_sm * thickness) / 1000), 3)


street = Road(10000,500)
print(street)
print(type(street))
print(street._lenght)
print(street._width)
print(street.asf_mas(30, 10))
street2 = Road(9900,30)
print(street2._lenght)
print(street2._width)
print(street2.asf_mas(25, 5))
