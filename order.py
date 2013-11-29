import json
from item import Item

class Order(object):
    

    def __init__(self, order_dict):
        self.id = order_dict['id']
        self.user_id =order_dict['user_id']
        self.items = []
        for item_dict in order_dict['items']:
            self.items.append(Item(item_dict))

    def number_of_items(self):
    	return len(self.items)
