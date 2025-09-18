import unittest
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

class TestFigures(unittest.TestCase):
    def test_rectangle_area(self):
        r = Rectangle(2, 3, "синий")
        self.assertEqual(r.area(), 6)

    def test_circle_area(self):
        c = Circle(2, "зеленый")
        self.assertAlmostEqual(c.area(), 12.566, places=3)

    def test_square_area(self):
        s = Square(3, "красный")
        self.assertEqual(s.area(), 9)
