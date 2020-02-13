# https://www.practicepython.org/exercise/2017/02/28/35-birthday-months.html

import json
from collections import Counter

def read_from_json(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

if __name__=='__main__':
    months = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
            }

    json_file = 'birthdays.json'
    d = read_from_json(json_file)
    month = []
    for name, bday in d.items():
        month.append(months[int(bday.split('/')[0])])

    count_month = Counter(month)
    print('Month = Birthday Count\n======================')
    for i in count_month:
        print(f'{i} = {count_month[i]}')
