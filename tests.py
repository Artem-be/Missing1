import unittest
import  zadanie1
from zadanie1 import offset


class TestSum(unittest.TestCase):
    def setUp(self):
        self.number = offset

    def test_sum1(self):
        self.assertTrue(type(self.number) is int)
    def test_sum2(self):
        self.assertTrue(type(self.number) is int)
    def test_sum3(self):
        self.assertFalse(type(self.number) is float)
    def test_sum4(self):
        self.assertFalse(type(self.number) is str)



    if __name__ == '__main__':

        test_sum1()
        test_sum2()
        test_sum3()
        test_sum4()

        print("Everything passed")