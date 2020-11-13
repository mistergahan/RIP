from main import Box1, Box2
import unittest


class SummaTest(unittest.TestCase):
    def test_sum_Box1(self):
        order = Box1()
        order.add_all()
        self.assertEqual(order.box.get_sum(), 365, "Should be 365")

    def test_sum_Box2(self):
        order = Box2()
        order.add_all()
        self.assertEqual(order.box.get_sum(), 415, "Should be 415")


if __name__ == "__main__":
    unittest.main()
