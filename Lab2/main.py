from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import arrow


def main():
    r = Rectangle("синего", 5, 6)
    c = Circle("красного", 11)
    s = Square("желтого", 11)

    utc_time = arrow.utcnow()
    print('Времечко у нас такое вот (UTC): ', utc_time)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()