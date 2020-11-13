from abc import ABC, abstractmethod
from main import Box1, Box2


class Component(ABC):
    """
        Базовый класс Компонент объявляет общие операции как для простых, так и для
        сложных объектов структуры.
    """
    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def is_composite(self):
        return False

    @abstractmethod
    def operation(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class Leaf(Component):
    """Конечный объект, не имеющий вложенных."""
    def __init__(self, value, price):
        self._value = value
        self._price = price

    def operation(self):
        return self._value

    def get_price(self):
        return self._price


class Composite(Component):
    """Объект, имеющий вложенные объекты."""
    def __init__(self, name):
        self._children = []
        self._name = name

    def add(self, component):
        self._children.append(component)
        component.parent = self

    def remove(self, component):
        self._children.remove(component)
        component.parent = None

    def is_composite(self):
        return True

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return self._name+f"({'+'.join(results)})"

    def get_price(self):
        count = 0
        for child in self._children:
            count += child.get_price()
        return count


def client_code(component):
    print(f"Box: {component.operation()}")
    print(f'Общая стоимость: {component.get_price()}', end='\n\n')


if __name__=='__main__':
    menu = Composite('Меню')
    drinks = Composite('Напитки')
    drinks.add(Leaf('Яблочный сок', 100))
    drinks.add(Leaf('Чай чёрный', 50))
    boxes = Composite('Боксы')
    box1 = Box1()
    box1.add_all()
    box2 = Box2()
    box2.add_all()
    boxes.add(Leaf(box1.box.list_box(), box1.box.get_sum()))
    boxes.add(Leaf(box2.box.list_box(), box2.box.get_sum()))
    paper = Leaf('Салфетка', 15)

    menu.add(drinks)
    menu.add(boxes)
    menu.add(paper)

    client_code(menu)
    client_code(boxes)
    client_code(paper)
    client_code(drinks)
