# https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html

birthday_dict = {
        'Albert Einstein': '03/14/1879',
        'Ada Lovelace': '12/10/1815',
        'Benjamin Franklin': '01/17/1706'
        }

if __name__=='__main__':
    print(f'Welcome to the birthday dictionary. I know the birthdays of: ')
    for name in birthday_dict:
        print(name)

    user = input('Whose birthday do you want to look up?\n')
    if user in birthday_dict:
        print(f'{user}\'s birthday is {birthday_dict[user]}.')
    else:
        print(f'Sorry, I don\'t know.')
