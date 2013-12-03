from order import Order
import json

class Parser:

	def __init__(self, orders_json):
		self.order_list = json.loads(orders_json)

	def biggest_order(self):
		max_value = 0
		for order_dict in self.order_list:
			order = Order(order_dict)
			if max_value < order.number_of_items():
				max_value = order.number_of_items()

		return max_value
		

	def most_expensive_order(self):
	    order_total_price = 0
	    for order_json in self.order_list:
	        order = Order(order_json)
	        if order_total_price < order.total_price():
	            most_expensive_order = order

	    return most_expensive_order

