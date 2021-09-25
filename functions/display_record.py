import database


def display_records():
    for user in database.users_database:
        print(f"""
=================================
ACCOUNT:

name: {user['name']}
username: {user['username']}
password: {user['password']}
=================================
""")


def display_record(username):
    for user in database.users_database:
        if user['username'] == username:
            print(f"""
=================================
ACCOUNT:

name: {user['name']}
username: {user['username']}
password: {user['password']}
=================================
""")
