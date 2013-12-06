from order import Order
import json

class Parser:
	def __init__(self, orders_json):
		order_dict_list = json.loads(orders_json)
		self.order_list = []
		for order_dict in order_dict_list:
			self.order_list.append(Order(order_dict))

	def biggest_order(self):
		max_value = 0
		for order in self.order_list:
			if max_value < order.number_of_items():
				max_value = order.number_of_items()

		return max_value

	def order_list_with_num_of_items(self, num_of_items):
		biggest_order_list = []
		for order in self.order_list:
			if order.number_of_items() == num_of_items:
				biggest_order_list.append(order)

		return biggest_order_list


	def most_expensive_order(self):
	    order_total_price = 0
	    for order in self.order_list:
	        if order_total_price < order.total_price():
	            most_expensive_order = order

	    return most_expensive_order

