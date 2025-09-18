from .figure import Figure
from .color import FigureColor
import math

class Circle(Figure):
    name = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor(color)

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return "Фигура: {}; Радиус: {}; Цвет: {}; Площадь: {:.2f}".format(
            self.get_name(), self.radius, self.color.color, self.area()
        )
