import users_wrapper as users

user = users.read(1)
print(user["name"])
users_list = users.list()
print(users_list)

users.delete(1)
