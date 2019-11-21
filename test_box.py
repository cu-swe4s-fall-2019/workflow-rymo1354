import unittest
import random
import os
import box


class TestBox(unittest.TestCase):
    def test_boxplot(self):
        rand1 = [random.randint(0, 10) for i in range(10)]
        rand2 = [random.randint(0, 10) for i in range(10)]
        rand3 = [random.randint(0, 10) for i in range(10)]
        data = [[rand1, rand2, rand3]]
        meta = ['rand1', 'rand2', 'rand3']
        title = ['Random Number Distribution']
        box.boxplot(data, meta, 'Random Numbers', title, 'rand.png')
        self.assertTrue(os.path.exists('rand.png'))
        os.remove('rand.png')


if __name__ == '__main__':
    unittest.main()
