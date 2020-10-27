from lab32 import gen_random

class Unique:
    """Возвращает итератор, который принимает на вход массив или
     генератор items и итерируется по элементам, пропуская дубликаты.
     Также может принимать булевый параметр ignore_case. Если ignore_case =
     True, то регистр игнорируется (то есть 'a' и 'A' - одно и тоже,
     иначе - регистр учитывается (то есть 'a' и 'A' - разные символы.
     По умолчанию ignore_case = False."""
    def __init__(self, items, **kwargs):
        self.used_elements = set()  # применяется для хранения уникальных элементов items
        self.data = list(items)
        self.index = 0  # применяется для отслеживания индекса итерируемого элемента в items
        if 'ignore_case' in kwargs.keys():
            self.ignore_case = kwargs['ignore_case']
        else:
            self.ignore_case = False

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            current = self.data[self.index]
            self.index += 1
            if ((self.ignore_case or not isinstance(current, str))
                    and current not in self.used_elements):
                self.used_elements.add(current)
                return current
            elif (not self.ignore_case and isinstance(current, str)
                    and current.upper() not in self.used_elements
                    and current.lower() not in self.used_elements):
                self.used_elements.add(current.upper())
                self.used_elements.add(current.lower())
                return current

    def __iter__(self):
        return self


if __name__ == '__main__':
    data_int = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data_rand = gen_random(10, 3, 10)  # генерируется 10 случайных чисел от 3 до 10
    data_str = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print('Отбор уникальных чисел: ', str(list(Unique(data_int)))[1:-1])
    print('Отбор уникальных случайных чисел: ', str(list(Unique(data_rand)))[1:-1])
    print('Отбор уникальных строк без игнорирования регистра по умолчанию: ', str(list(Unique(data_str)))[1:-1])
    print('Отбор уникальных строк с игнорированием регистра: ', str(list(Unique(data_str, ignore_case=True)))[1:-1])
    print('Отбор уникальных строк без игнорирования регистра: ', str(list(Unique(data_str, ignore_case=False)))[1:-1])
