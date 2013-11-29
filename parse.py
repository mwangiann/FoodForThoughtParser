import json
import urllib2
from item import Item
from order import Order 

#orders_json = '[{"id":1,"created_at":"2013-10-06T09:55:46.385Z","updated_at":"2013-10-10T15:08:15.198Z","user_id":7,"items":[{"id":4,"name":"Another item","price":1000,"created_at":"2013-09-30T19:08:53.228Z","updated_at":"2013-10-20T10:02:56.701Z","available":true,"item_type":"food"}]},{"id":2,"created_at":"2013-10-06T09:55:46.396Z","updated_at":"2013-10-10T15:08:15.201Z","user_id":7,"items":[{"id":2,"name":"Pizza","price":3000,"created_at":"2013-09-29T11:20:31.997Z","updated_at":"2013-10-10T11:57:59.212Z","available":false,"item_type":"food"}]},{"id":3,"created_at":"2013-10-06T09:55:46.401Z","updated_at":"2013-10-10T15:08:15.203Z","user_id":7,"items":[{"id":2,"name":"Pizza","price":3000,"created_at":"2013-09-29T11:20:31.997Z","updated_at":"2013-10-10T11:57:59.212Z","available":false,"item_type":"food"}]},{"id":4,"created_at":"2013-10-06T09:55:46.405Z","updated_at":"2013-10-10T15:08:15.205Z","user_id":7,"items":[{"id":2,"name":"Pizza","price":3000,"created_at":"2013-09-29T11:20:31.997Z","updated_at":"2013-10-10T11:57:59.212Z","available":false,"item_type":"food"},{"id":8,"name":"Chicken","price":5000,"created_at":"2013-10-04T07:46:12.103Z","updated_at":"2013-10-20T10:02:56.703Z","available":true,"item_type":"meat"},{"id":10,"name":"Beer","price":3000,"created_at":"2013-10-04T07:46:34.873Z","updated_at":"2013-10-20T10:02:56.702Z","available":true,"item_type":"drink"}]},{"id":5,"created_at":"2013-10-06T09:55:46.411Z","updated_at":"2013-10-10T15:08:15.206Z","user_id":7,"items":[{"id":9,"name":"Beef","price":5000,"created_at":"2013-10-04T07:46:18.611Z","updated_at":"2013-10-10T11:57:59.217Z","available":false,"item_type":"meat"}]},{"id":6,"created_at":"2013-10-06T10:06:27.506Z","updated_at":"2013-10-10T15:08:15.207Z","user_id":7,"items":[{"id":2,"name":"Pizza","price":3000,"created_at":"2013-09-29T11:20:31.997Z","updated_at":"2013-10-10T11:57:59.212Z","available":false,"item_type":"food"},{"id":8,"name":"Chicken","price":5000,"created_at":"2013-10-04T07:46:12.103Z","updated_at":"2013-10-20T10:02:56.703Z","available":true,"item_type":"meat"},{"id":10,"name":"Beer","price":3000,"created_at":"2013-10-04T07:46:34.873Z","updated_at":"2013-10-20T10:02:56.702Z","available":true,"item_type":"drink"}]},{"id":10,"created_at":"2013-10-10T11:57:59.200Z","updated_at":"2013-10-10T15:08:15.208Z","user_id":7,"items":[{"id":2,"name":"Pizza","price":3000,"created_at":"2013-09-29T11:20:31.997Z","updated_at":"2013-10-10T11:57:59.212Z","available":false,"item_type":"food"},{"id":8,"name":"Chicken","price":5000,"created_at":"2013-10-04T07:46:12.103Z","updated_at":"2013-10-20T10:02:56.703Z","available":true,"item_type":"meat"},{"id":9,"name":"Beef","price":5000,"created_at":"2013-10-04T07:46:18.611Z","updated_at":"2013-10-10T11:57:59.217Z","available":false,"item_type":"meat"}]},{"id":11,"created_at":"2013-10-10T15:17:53.655Z","updated_at":"2013-10-10T15:17:53.655Z","user_id":7,"items":[{"id":11,"name":"This is a long item","price":1000,"created_at":"2013-10-04T07:52:15.889Z","updated_at":"2013-10-20T10:02:56.700Z","available":true,"item_type":"drink"},{"id":13,"name":"Veggie","price":2000,"created_at":"2013-10-04T16:12:22.997Z","updated_at":"2013-10-10T15:17:53.717Z","available":false,"item_type":"vegetable"},{"id":12,"name":"Test meat item","price":1000,"created_at":"2013-10-04T16:11:52.087Z","updated_at":"2013-10-20T10:02:56.706Z","available":true,"item_type":"meat"}]},{"id":12,"created_at":"2013-10-10T15:17:53.684Z","updated_at":"2013-10-10T15:17:53.684Z","user_id":7,"items":[{"id":2,"name":"Pizza","price":3000,"created_at":"2013-09-29T11:20:31.997Z","updated_at":"2013-10-10T11:57:59.212Z","available":false,"item_type":"food"},{"id":9,"name":"Beef","price":5000,"created_at":"2013-10-04T07:46:18.611Z","updated_at":"2013-10-10T11:57:59.217Z","available":false,"item_type":"meat"},{"id":8,"name":"Chicken","price":5000,"created_at":"2013-10-04T07:46:12.103Z","updated_at":"2013-10-20T10:02:56.703Z","available":true,"item_type":"meat"}]},{"id":13,"created_at":"2013-10-10T15:17:53.692Z","updated_at":"2013-10-10T15:17:53.692Z","user_id":7,"items":[{"id":10,"name":"Beer","price":3000,"created_at":"2013-10-04T07:46:34.873Z","updated_at":"2013-10-20T10:02:56.702Z","available":true,"item_type":"drink"},{"id":9,"name":"Beef","price":5000,"created_at":"2013-10-04T07:46:18.611Z","updated_at":"2013-10-10T11:57:59.217Z","available":false,"item_type":"meat"},{"id":15,"name":"Meat Item","price":5000,"created_at":"2013-10-07T15:48:52.017Z","updated_at":"2013-10-20T10:02:56.705Z","available":true,"item_type":"meat"}]},{"id":14,"created_at":"2013-10-10T15:17:53.702Z","updated_at":"2013-10-10T15:17:53.702Z","user_id":4,"items":[{"id":13,"name":"Veggie","price":2000,"created_at":"2013-10-04T16:12:22.997Z","updated_at":"2013-10-10T15:17:53.717Z","available":false,"item_type":"vegetable"},{"id":8,"name":"Chicken","price":5000,"created_at":"2013-10-04T07:46:12.103Z","updated_at":"2013-10-20T10:02:56.703Z","available":true,"item_type":"meat"},{"id":15,"name":"Meat Item","price":5000,"created_at":"2013-10-07T15:48:52.017Z","updated_at":"2013-10-20T10:02:56.705Z","available":true,"item_type":"meat"}]}]'
# fft_data = urllib2.urlopen('http://tw-food-for-thought.herokuapp.com/information/orders.js')
# self.fft_orders = json.load(fft_data)
orders_json = urllib2.urlopen('http://tw-food-for-thought.herokuapp.com/information/orders.js')
list = json.load(orders_json)


#for element in list:
 #   print len(element['items'])
  #  print element['user_id']

#print len(list[0]['items']

#Item.new(orders[0]['items'][0]))

#load each order into an order object

#have some parser object that can find, given a list of orders, the user id of the order with the most items

orders_list = []

for order_dict in list:
    orders_list.append(Order(order_dict))
    

# for order in orders_list:
#     print "user: " + str(order.user_id) + "  number of order items: " + str(order.number_of_items())


def biggest_order():
        max_value = 0
        for order_hash in list:
            order = Order(order_hash)
            if max_value < order.number_of_items():
                max_value = order.number_of_items()
        return max_value

print "max no of items " + str(biggest_order())

def most_expensive_order():
    total_price = 0
    for order_hash in list:








