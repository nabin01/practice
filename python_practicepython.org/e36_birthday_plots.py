# https://www.practicepython.org/exercise/2017/04/02/36-birthday-plots.html

import json
from collections import Counter
from bokeh.models.annotations import Title
from bokeh.plotting import figure, show, output_file

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

    output_file('plot.html')
    p = figure(x_range = list(months.values()))
    p.vbar(x = [x for x in count_month.keys()], top = [y for y in count_month.values()], width = 0.5)
    p_title = Title()
    p_title.text = 'Birthday Count by Months'
    p.title = p_title
    show(p)
