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

	def user_who_ordered_most_of(self, item_id): # n.b: yet to be refactored
		order_item_list = []
		for order in order_list:
			if len(filter (lambda x : x.item_id == item_id, order.items)) > 0:
				order_item_list.append(order)

		user_and_no_ordered = {}
		for order in order_item_list:
			if user_and_no_ordered.has_key(order.user_id):
				user_and_no_ordered[order.user_id] = user_and_no_ordered[order.user_id] + 1
			else:
				user_and_no_ordered.append(order.user_id, 1)

		max_no_ordered =  max(user_and_no_ordered.values())

		users_with_max_orders = {}

		for key, value in user_and_no_ordered.items():
			if value == max_no_ordered:
				users_with_max_orders = {key, value}

		return users_with_max_orders





			
