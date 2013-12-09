import json
import urllib2
from src.item import Item
from src.order import Order
from src.parser import Parser
from src.user_list import UserList



#orders_json = urllib2.urlopen('http://tw-food-for-thought.herokuapp.com/information/orders.js')

with open('orders_json_backup', 'r') as f:
    orders_json = f.read()

parser = Parser(orders_json)

with open('users_json_backup', 'r') as f:
    users_json = f.read()

user_list = UserList(users_json)

#print "biggest order is: " + str(parser.biggest_order())

#for order in parser.order_list_with_num_of_items(9):
#	print "User: " + user_list.user_by_id(order.user_id)['username']

users_who_have_paid_highest = parser.user_who_has_paid_highest();	

#print "The maximum amount paid is: " + str(users_who_have_paid_highest.)
for key,value in users_who_have_paid_highest.iteritems():
	print "The person who has paid the highest amount of money is: " + user_list.user_by_id(key)["username"] + "  Amount paid: " + str(value)


#print "user 1 is: " + user_list.user_by_id(5)['username']

#for element in list:
 #   print len(element['items'])
  #  print element['user_id']

#print len(list[0]['items']

#Item.new(orders[0]['items'][0]))

#load each order into an order object

#have some parser object that can find, given a list of orders, the user id of the order with the most items
