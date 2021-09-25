import database
from functions import display_record


def edit_account():
    print("""
    =================================
           Account Edit Secton
    =================================
    """)

    user_input = get_input()

    for user in database.users_database:
        if user['username'] == user_input:
            new_name = input('Enter new name: ')
            new_username = input('Enter new username: ')
            new_password = input('Enter new password: ')
            user['name'] = new_name
            user['username'] = new_username
            user['password'] = new_password
        else:
            print("Account does not exist.")


def get_input():
    user_input = input("Enter username to edit account: ")
    display_record.display_record(user_input)
    return user_input
