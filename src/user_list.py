import json

class UserList:
	def __init__(self, users_json):
		self.user_list = json.loads(users_json)

	def user_by_id(self, user_id):
		for user in self.user_list:
			if user['id'] == user_id:
				return user

