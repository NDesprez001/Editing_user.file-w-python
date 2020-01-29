import json


## ORIGINAL USERS.FILE

# users = [
#   {
#     'first_name': 'John',
#     'last_name': 'Smith',
#     'address': '123 NW 45 Ave',
#     'email': 'johns@gmail.com',
#     'password': 'jjj333'
#   },
#   {
#     'first_name': 'Rachel',
#     'last_name': 'Smith',
#     'address': '1 NW 4 Ave',
#     'email': 'rrr@gmail.com',
#     'password': 'rr55'
#   },
#   {
#     'first_name': 'Zion',
#     'last_name': 'Something',
#     'address': '12345 NW 777 Ave',
#     'email': 'zion@gmail.com',
#     'password': 'zion67'
#   },
#   {
#     'first_name': 'Jules',
#     'last_name': 'Verne',
#     'address': '7654 NW 99 Ave',
#     'email': 'julesv@gmail.com',
#     'password': 'verne900'
#   },
# ]
# with open('users.json','w') as jfile:
#   json.dump(users, jfile)



## LOGIN_FUNCTION 

# with open('users.json','r') as jfile:
#   info = json.load(jfile)

# def login():
#   username = input('Enter username here:')
#   password = input('Enter password here:')
#   with open('users.json','r') as jfile:
#     info = json.load(jfile)

#   user_found = False
#   for d in info:
#     if d['first_name'] == username and d['password'] == password:
#       print('Access granted')
#       print(d)
#       user_found = True
#   if not user_found:
#     print("User not found 404")
      
# login()

## LOGIN_FUNCTION (version 2)

# with open('users.json','r') as jfile:
#   users = json.load(jfile)

# def login(a, b):
#   for user in users:
#     if user['first_name'] == a and user['password'] == b:
#       return user
#   return None

# username = input('Enter username: ')
# password = input('Enter password: ')

# response = login(username, password)

# if response is not None:
#   print("Welcome " + response['first_name'] + response['last_name'])
#   print(response)
# else:
#   print('User not found 404')

## REGISTER_FUNCTION (add/creating a new user)

with open('users.json','r') as jfile:
   user = json.load(jfile)


def register(a):
  user.append(a)
  print('Successfully added')


first_name = input('Enter first name: ')
last_name = input('Enter last name: ')
email = input('Enter email: ')
address = input('Enter address: ')
password = input('Enter password: ')

new_user = {
  'first_name': first_name,
  'last_name': last_name,
  'email': email,
  'address': address,
  'password': password
}
register(new_user)


with open('users.json','w') as jfile:
  json.dump(user, jfile)
