import unittest
import json
from item import Item
from order import Order

class TestParser(unittest.TestCase):

    def setUp(self):
        order_json = '{"id":1,"created_at":"2013-10-06T09:55:46.385Z","updated_at":"2013-10-10T15:08:15.198Z","user_id":7,"items":[{"id":4,"name":"Another item","price":1000,"created_at":"2013-09-30T19:08:53.228Z","updated_at":"2013-10-20T10:02:56.701Z","available":true,"item_type":"food"}]}'
        self.order_hash = json.loads(order_json)

    def test_item_should_load_from_hash(self):
        item = Item(self.order_hash['items'][0])
        self.assertEqual(item.id, 4)
        self.assertEqual(item.name, "Another item")
        self.assertEqual(item.price, 1000)
        self.assertEqual(item.available,True)

    def test_order_should_load_from_hah(self):
        order = Order(self.order_hash)
        self.assertEqual(order.id,1)
        self.assertEqual(order.user_id,7)
        self.assertEqual(order.items[0].id, 4)
    def test_no_of_order_items(self):
        order = Order(self.order_hash)
        self.assertEqual(len(order.items),1)


if __name__ == '__main__':
    unittest.main()
