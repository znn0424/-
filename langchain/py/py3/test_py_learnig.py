import unittest
from unittest import TestCase
from py_learning import ShoppingList
class Test(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({"英语书":10,"数学书":12})

    def test_item_count(self):
        self.assertEqual(self.shopping_list.item_count(), 2)

    def test_price_count(self):
        self.assertEqual(self.shopping_list.price_count(), 22)