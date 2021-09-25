from functions import add_account, display_record, edit_account, delete_account, search_account


def main_menu():
    print(
        """
    =================================
    Account Registration
         Menu

    [A] - Add
    [E] - Edit
    [D] - Delete
    [S] - Search
    [R] - Display Record
    =================================
    """
    )

    user_input = get_input()

    if user_input.lower() == 'a':
        add()

    if user_input.lower() == 'r':
        display()

    if user_input.lower() == 'e':
        edit()

    if user_input.lower() == 'd':
        delete()

    if user_input.lower() == 's':
        search()


def get_input():
    user_input = input('Choose: ')
    return user_input


def add():
    add_account.add_account()
    main_menu()


def edit():
    edit_account.edit_account()
    main_menu()


def delete():
    delete_account.delete_account()
    main_menu()


def search():
    search_account.search_account()
    main_menu()


def display():
    try:
        display_record.display_records()
    except KeyError:
        print('Account does not exist')
    finally:
        main_menu()


main_menu()
