import database
from functions import display_record


def search_account():
    print("""
    ==============================
        Account Registration
            Search Account
    ==============================
    """)

    user_input = get_input()

    for user in database.users_database:
        if user['username'] == user_input:
            display_record.display_record(user_input)


def get_input():
    user_input = input("Enter Username to search an account: ")
    return user_input
