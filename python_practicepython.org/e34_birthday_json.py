# https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html

import json

def read_from_json(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

def write_to_json(json_file, to_dump):
    feeds = read_from_json(json_file)
    with open(json_file, 'w') as f:
        feeds.update(to_dump)
        print(feeds)
        json.dump(feeds, f, indent=2)

def list_all():
    print('Name = Birthday\n===============')
    for name, birthday in read_from_json(json_file).items():
        print(f'{name} = {birthday}')

def search_birthday():
    user = input("Whose birthday do you want to know? ")
    birthday_dict = read_from_json(json_file)
    if user in birthday_dict:
        print(f'{user}\'s birthday is {birthday_dict[user]}.')
    else:
        print(f'Sorry, I don\'t know.')

def add_birthday():
    name = input("Enter the name: ")
    birthday = input("Enter birthday: ")
    write_to_json(json_file, {name: birthday})

if __name__=='__main__':
    json_file = 'birthdays.json'
    print(f'\nWelcome to the birthday dictionary.\nPlease choose one of the following: ') 
    while True:
        print('\n1. List all names\n2. Search birthday\n3. Add Birthday\n4. Exit\nPlease choose one: ')
        user_menu = input()
        if user_menu == '1':
            list_all()
        elif user_menu == '2':
            search_birthday()
        elif user_menu == '3':
            add_birthday()
        elif user_menu == '4':
            print("Thanks for stopping by!")
            break
        else:
            print("Please enter a valid option.")
 
