from abc import ABC, abstractmethod

class Figure(ABC):
    name = "Геометрическая фигура"

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    def get_name(self):
        return self.name
