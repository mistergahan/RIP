from main1 import Composite, Component, Leaf, client_code
from main import Box1, Box2
from abc import ABC, abstractmethod


class ComponentNew(Component):
    """
        Интерфейс Компонента объявляет метод accept, который в качестве аргумента
        может получать любой объект, реализующий интерфейс посетителя.
    """
    @abstractmethod
    def accept(self, visitor):
        pass


class CompositeNew(Composite, ComponentNew):
    def accept(self, visitor):
        visitor.visit_component(self)


class Visitor(ABC):
    @abstractmethod
    def visit_component(self, element):
        pass


class Visitor1(Visitor):
    def visit_component(self, element):
        print('Стоимость: {}'.format(element.get_price()))


class Visitor2(Visitor):
    def visit_component(self, element):
        client_code(element)


if __name__ == '__main__':
    menu = CompositeNew('Меню')
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

    visitor1 = Visitor1()
    visitor2 = Visitor2()
    print("Первый посетитель:")
    menu.accept(visitor1)
    print("\nВторой посетитель:")
    menu.accept(visitor2)
