class FigureColor:
    def __init__(self, color: str):
        self._color = color

    @property
    def color(self):
        return self._color

    def __repr__(self):
        return f"Цвет: {self._color}"
