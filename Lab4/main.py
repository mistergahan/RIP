from abc import ABC, abstractmethod, abstractproperty

class Box(ABC):
    """
        Интерфейс Строителя объявляет создающие методы для различных частей объектов
        Продуктов.
    """
    @abstractproperty
    def box(self):
        """Продуктом является бокс."""
        pass

    @abstractmethod
    def add_burger(self):
        pass

    @abstractmethod
    def add_potatoe(self):
        pass

    @abstractmethod
    def add_salad(self):
        pass

    @abstractmethod
    def add_drink(self):
        pass

class Box1(Box):
    """Конкретный строитель, строящий бокс первого типа."""
    def __init__(self):
        self.reset()

    def reset(self):
        self._box = Boxx()

    @property
    def box(self):
        box = self._box
        return box

    def add_burger(self):
        self._box.add("Двойной чизбургер", 110)

    def add_potatoe(self):
        self._box.add("Кортошка Фри", 50)

    def add_salad(self):
        self._box.add("Салат \"Цезарь\"", 125)

    def add_drink(self):
        self._box.add("Яблочный сок", 80)

    def add_all(self):
        self.add_burger()
        self.add_potatoe()
        self.add_salad()
        self.add_drink()


class Box2(Box):
    """Конкретный строитель, строящий бокс второго типа."""
    def __init__(self):
        self.reset()

    def reset(self):
        self._box = Boxx()

    @property
    def box(self):
        box = self._box
        return box

    def add_burger(self):
        self._box.add("БигМак", 180)

    def add_potatoe(self):
        self._box.add("Картофель по-деревенски", 75)

    def add_salad(self):
        self._box.add("Салат \"Греческий\"", 100)

    def add_drink(self):
        self._box.add("Газировка", 60)

    def add_all(self):
        self.add_burger()
        self.add_potatoe()
        self.add_salad()
        self.add_drink()


class Boxx():
    def __init__(self):
        self.box = []
        self.sum = 0

    def add(self, dish, price):
        self.box.append(dish)
        self.sum += price

    def list_box(self):
        return f"{', '.join(self.box)}"

    def get_sum(self):
        return self.sum


if __name__ == '__main__':
    print('Комбо №1 ')
    order = Box1()
    order.add_burger()
    order.add_potatoe()
    order.add_drink()
    print(order.box.list_box())

    print('\nКомбо №2 ')
    order.reset()
    order.add_potatoe()
    order.add_salad()
    print(order.box.list_box())

    print('\nКомбо №3 ')
    order = Box2()
    order.add_all()
    print(order.box.list_box())
