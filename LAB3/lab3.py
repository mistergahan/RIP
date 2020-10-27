from typing import List  # необходим для задания типа для аннотации типов


def field(items: List[dict], *args: str) -> iter:
    """Создает генератор для отбора записей в списке словарей
    items по ключам, указанным в args."""
    assert len(args) > 0
    if len(args) == 1:
        for i in items:
            if args[0] in i.keys() and not i[args[0]] is None:
                yield i[args[0]]
    else:
        for i in items:
            temp_dict = {}
            for key in args:
                if key in i.keys() and not i[key] is None:
                    temp_dict[key] = i[key]
            if len(temp_dict) > 0:
                yield temp_dict


if __name__ == '__main__':
    goods = [
        {'title': 'Шапка', 'price': 1500, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
        {'color':'black'}
    ]
    print(str(list(field(goods, 'title')))[1:-1])
    print(str(list(field(goods, 'title', 'price')))[1:-1])
