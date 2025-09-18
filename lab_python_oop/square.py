from .rectangle import Rectangle

class Square(Rectangle):
    name = "Квадрат"

    def __init__(self, side, color):
        super().__init__(side, side, color)

    def __repr__(self):
        return "Фигура: {}; Сторона: {}; Цвет: {}; Площадь: {:.2f}".format(
            self.get_name(), self.width, self.color.color, self.area()
        )
