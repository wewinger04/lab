import unittest
from classes import *

class TestClasses(unittest.TestCase):
    def test___init__(self):
        tv_1 = Television()
        if (tv_1.__channel == 0) and (tv_1.__volume == 0) and (tv_1.__is_on == False):
            expected = True
        else:
            expected = False
        self.assertEqual(expected, True)
    
    def test_power(self):
        tv_1.power()
        if tv_1.__is_on == True:
            expected = True
        else:
            expected = False
        self.assertEqual(expected, True)
    
    def test_channel_up(self):
        tv_1.channel_up()
        tv_1.channel_up()
        if tv_1.channel == 2:
            expected = True
        else:
            actual = False
        self.assertEqual(expected, True)
        
    def test_channel_down(self):
        tv_1.channel_down()
        if tv_1.channel == 1:
            expected = True
        else:
            actual = False
        self.assertEqual(expected, True)
        
    def test_volume_up(self):
        tv_1.volume_up()
        tv_1.volume_up()
        if tv_1.volume == 2:
            expected = True
        else:
            actual = False
        self.assertEqual(expected, True)
    
    def test_volume_down(self):
        tv_1.volume_down()
        if tv_1.volume == 1:
            expected = True
        else:
            actual = False
        self.assertEqual(expected, True)

    def main():
        tv_1 = Television()
        tv_1.test___init__()
        tv_1.test_power()
        tv_1.test_channel_up()
        tv_1.test_channel_down()
        tv_1.test_volume_up()
        tv_1.test_volume_down()

if __name__ == '__main__':
    main()