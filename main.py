import requests
from bs4 import BeautifulSoup
import texttable

URL = 'https://www.worldometers.info/coronavirus/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table')

headers = ['lp', 'Country', 'Cases', 'Population', 'Infected%', 'Infected% but nicer']
cells = []
rows = table.findAll('tr')

def bubblesort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j][4] < arr[j + 1][4]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


for tr in rows[1:-2]:
    row = []
    td = tr.findAll('td')
    row.append(td[0].text)
    row.append(td[1].text)
    row.append(td[2].text)
    row.append(td[14].text)
    var1 = td[2].text.replace(',', '').replace(' ', '')
    var2 = td[14].text.replace(',', '').replace(' ', '')
    if var1 == '' or var2 == '':
        continue
    row.append((int(var1) * 100 / int(var2)))
    row.append(str(round(int(var1) * 100 / int(var2), 2)) + '%')
    if row[0] != '':
        cells.append(row)


def show_table(headers, cells, footer):
    table = texttable.Texttable()
    table.header(headers)
    for cell in cells:
        table.add_row(cell)
    retval = table.draw()
    return retval + '\n' + footer


bubblesort(cells)

lp = 1
for i in cells:
    i[0] = lp
    lp = lp + 1

print(show_table(headers, cells, ''))
