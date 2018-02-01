import unittest
from collections import namedtuple
from PageCollector import PageCollector

Product = namedtuple('Item', ['Id', 'Cost', 'Revenue', 'SellPrice'])

class PageCollectorTest(unittest.TestCase):
    products = (Product(Id=1,  Cost=1,  Revenue=11, SellPrice=21),
                Product(Id=2,  Cost=2,  Revenue=12, SellPrice=22),
                Product(Id=3,  Cost=3,  Revenue=13, SellPrice=23),
                Product(Id=4,  Cost=4,  Revenue=14, SellPrice=24),
                Product(Id=5,  Cost=5,  Revenue=15, SellPrice=25),
                Product(Id=6,  Cost=6,  Revenue=16, SellPrice=26),
                Product(Id=7,  Cost=7,  Revenue=17, SellPrice=27),
                Product(Id=8,  Cost=8,  Revenue=18, SellPrice=28),
                Product(Id=9,  Cost=9,  Revenue=19, SellPrice=29),
                Product(Id=10, Cost=10, Revenue=20, SellPrice=30),
                Product(Id=11, Cost=11, Revenue=21, SellPrice=31))

    def test_page_num_3_for_Cost(self):
        #arrange
        sut = PageCollector(PageCollectorTest.products)
        expected = [6, 15, 24, 21]
        #act
        actual = list(sut.get_sum(lambda x: x.Cost, page_num=3))
        #assert
        self.assertEqual(actual, expected)

    def test_page_num_4_for_Revenue(self):
        #arrange
        sut = PageCollector(PageCollectorTest.products)
        expected = [50, 66, 60]
        #act
        actual = list(sut.get_sum(lambda x: x.Revenue, page_num=4))
        #assert
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(PageCollectorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
