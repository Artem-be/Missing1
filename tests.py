import unittest
import zadanie1
from zadanie1 import offset


class Test(unittest.TestCase):
    def setUp(self):
        self.number = offset

    def test1(self):
        self.assertTrue(type(self.number) is int)
    def test2(self):
        self.assertTrue(type(self.number) is int)
    def test3(self):
        self.assertFalse(type(self.number) is float)
    def test4(self):
        self.assertFalse(type(self.number) is str)



    if __name__ == '__main__':

        test1()
        test2()
        test3()
        test4()

        print("Everything passed")
