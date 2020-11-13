from main2 import *
import unittest


class SummaTest(unittest.TestCase):
    def test_summa_menu(self):
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
        self.assertEqual(menu.accept(visitor1), 'visitor_for_composite_new', "Should be 'visitor_for_composite_new'")


if __name__ == "__main__":
    unittest.main()
