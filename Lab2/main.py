from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import arrow


def main():
    r = Rectangle("синего", 11, 11)
    c = Circle("зеленого", 11)
    s = Square("красного", 11)

   # from datetime import datetime
   # dt = datetime.now()
    #arrow_dt = arrow.Arrow.formdate(dt)
   # print(dt)
    #print(arrow_dt)

    utc_time = arrow.utcnow()
    print('Времечко у нас такое вот (UTC): ',utc_time)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()