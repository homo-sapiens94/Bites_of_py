from collections import defaultdict
import os
from urllib.request import urlretrieve
from collections import defaultdict
from bs4 import BeautifulSoup


# prep data
holidays_page = os.path.join('/tmp', 'us_holidays.php')
urlretrieve('https://bit.ly/2LG098I', holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content,'html.parser')
    table = soup.find('table', attrs = {'class':'list-table'})

    d = defaultdict(list)


    holidays = []
    for row in table.findAll('a'):
    	holidays.append(row.text)
    
    months = []
    for row in table.findAll('time'):
    	months.append(row.text.split('-')[1])
    
    temp = list(zip(months,holidays))
    # print(temp)
    for month, holiday in temp:
    	d[month].append(holiday)
    return d
    


#pybites Solution


from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup


# prep data
holidays_page = os.path.join('/tmp', 'us_holidays.php')
urlretrieve('https://bit.ly/2LG098I', holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find_all("table", class_="list-table")

    # start at 2nd item ignoring header
    for tr in table[0].find_all('tr')[1:]:
        time = tr.find('time')
        href = tr.find('a')
        day = href.text
        yy, mm, dd = time.text.split('-')  # or use dt.striptime
        holidays[mm].append(day)

    return holidays