import json

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



with open('users.json','r') as jfile:
  info = json.load(jfile)

# for d in info:
#   if d['first_name'] == 'Rachel':
#     print(d)


def login():
  username = input('Enter username here:')
  password = input('Enter password here:')
  with open('users.json','r') as jfile:
    info = json.load(jfile)

  user_found = False
  for d in info:
    if d['first_name'] == username and d['password'] == password:
      print('Access granted')
      print(d)
      user_found = True
  if not user_found:
    print("User not found 404")
      
login()