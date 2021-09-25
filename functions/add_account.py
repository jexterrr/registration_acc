import database


def add_account():
    print(
        """
    Account Registration
         Add Account
    """
    )

    get_input()


def get_input():
    name = input('Enter your name: ')
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    store_to_DB(name, username, password)


def store_to_DB(name, username, password):
    user_dict = dict()
    user_dict['name'] = name
    user_dict['username'] = username
    user_dict['password'] = password

    database.users_database.append(user_dict)
