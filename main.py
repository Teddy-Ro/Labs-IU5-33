from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import numpy as np

N = 19  # Ваш номер варианта — измените на свой

if __name__ == "__main__":
    figures = [
        Rectangle(N, N, "синий"),
        Circle(N, "зеленый"),
        Square(N, "красный"),
    ]
    for f in figures:
        print(f)

    # Внешний пакет: вызов numpy
    print("Пример работы с numpy: массив квадратов", np.array([i**2 for i in range(N)]))