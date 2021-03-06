from user import User

users = [
    User(1, 'bob', 'asdf')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    #here 'identity' is the secrekey
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)