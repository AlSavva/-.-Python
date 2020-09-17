# Создать класс TrafficLight (светофор) и определить у него один атрибут color
# (цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках
# метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и
# вызвав описанный метод.

def color_circle(color):
    import turtle as t
    t.speed(0)
    t.hideturtle()
    num = [100, 0, -100]
    if color == 'red':
        my_colors = ['red', 'black', 'black']
    if color == 'yellow':
        my_colors = ['black', 'yellow', 'black']
    if color == 'green':
        my_colors = ['black', 'black', 'green']
    if color == 'black':
        my_colors = ['black'] * 3
    t.up()
    for i in range(3):
        t.goto(0, num[i])
        t.down()
        t.begin_fill()
        t.fillcolor(my_colors[i])
        t.circle(50)
        t.end_fill()
        t.up()


class TrafficLight:
    __color = ['red', 'yellow', 'green', 'yellow']

    def running(self):
        import turtle as t
        from time import sleep
        from itertools import cycle
        chek = 5
        time_list = iter(cycle([7, 2]))
        it_color = iter(cycle(TrafficLight._TrafficLight__color))
        for i in range(chek):
            color_circle(next(it_color))
            sleep(next(time_list))
        color_circle('black')
        t.up()
        t.goto(0, -175)
        t.write("The End! Clic to exit", align="center",
                font=("Arial", 12, "normal"))
        t.exitonclick()


tl = TrafficLight()
tl.running()
