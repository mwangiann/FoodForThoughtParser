import json
import urllib2
from item import Item
from order import Order
from parser import Parser



#orders_json = urllib2.urlopen('http://tw-food-for-thought.herokuapp.com/information/orders.js')

with open('orders_json_backup', 'r') as f:
    orders_json = f.read()

print "biggest order is: " + str(Parser(orders_json).biggest_order())

#for element in list:
 #   print len(element['items'])
  #  print element['user_id']

#print len(list[0]['items']

#Item.new(orders[0]['items'][0]))

#load each order into an order object

#have some parser object that can find, given a list of orders, the user id of the order with the most items
