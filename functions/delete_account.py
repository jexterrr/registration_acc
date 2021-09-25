import database


def delete_account():
    print("""
        Account Registration
            Delete Account

    """)
    user_input = get_input()

    for user in database.users_database:
        if user['username'] == user_input:
            del user['name']
            del user['username']
            del user['password']
            print('Account deleted!')


def get_input():
    user_input = input('Enter username of the account you want to delete: ')
    return user_input
