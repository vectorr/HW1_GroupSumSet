import unittest
from GroupSum import ItemGroup
from GroupSum import Item

class ItemGroupTest(unittest.TestCase):
    items = [Item(Id=1,  Cost=1,  Revenue=11, SellPrice=21),
             Item(Id=2,  Cost=2,  Revenue=12, SellPrice=22),
             Item(Id=3,  Cost=3,  Revenue=13, SellPrice=23),
             Item(Id=4,  Cost=4,  Revenue=14, SellPrice=24),
             Item(Id=5,  Cost=5,  Revenue=15, SellPrice=25),
             Item(Id=6,  Cost=6,  Revenue=16, SellPrice=26),
             Item(Id=7,  Cost=7,  Revenue=17, SellPrice=27),
             Item(Id=8,  Cost=8,  Revenue=18, SellPrice=28),
             Item(Id=9,  Cost=9,  Revenue=19, SellPrice=29),
             Item(Id=10, Cost=10, Revenue=20, SellPrice=30),
             Item(Id=11, Cost=11, Revenue=21, SellPrice=31)]

    def test_group_of_3_for_Cost(self):
        #arrange
        sut = ItemGroup(ItemGroupTest.items)
        expected = [6, 15, 24, 21]
        #act
        actual = sut.get_group_sum_set(tag='Cost', num_of_a_group=3)
        #assert
        self.assertEqual(actual, expected)

    def test_group_of_4_for_Revenue(self):
        #arrange
        sut = ItemGroup(ItemGroupTest.items)
        expected = [50, 66, 60]
        #act
        actual = sut.get_group_sum_set(tag='Revenue', num_of_a_group=4)
        #assert
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ItemGroupTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
