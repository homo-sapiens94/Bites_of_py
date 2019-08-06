from pathlib import Path
from urllib.request import urlretrieve
import xml.etree.ElementTree as ET
from collections import defaultdict
# import the countries xml file
tmp = Path('/tmp')
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve('https://bit.ly/2IzGKav', countries)


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    tree = ET.parse(xml)
    root = tree.getroot()
    
    d= defaultdict(list)
    lst= []
    for country in root.findall('{http://www.worldbank.org}country'):	
    	name = country.find('{http://www.worldbank.org}name')
    	income = country.find('{http://www.worldbank.org}incomeLevel')
    	lst.append((income.text,name.text))
    #print(lst)
    for income,name in lst:
    	d[income].append(name)
    #print(d)
    
    return d










# Pybites Solution

from collections import defaultdict
from pathlib import Path
import xml.dom.minidom as md
from urllib.request import urlretrieve

# import the countries xml file
tmp = Path('/tmp')
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve('https://bit.ly/2IzGKav', countries)


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    with open(xml) as f:
        xmlstring = f.read()

    dom = md.parseString(xmlstring)
    incomes = defaultdict(list)

    for elem in dom.getElementsByTagName("wb:country"):
        wb_name = elem.getElementsByTagName('wb:name')
        country = wb_name[0].childNodes[0].data

        wb_income = elem.getElementsByTagName('wb:incomeLevel')
        income = wb_income[0].childNodes[0].data

        incomes[income].append(country)

    return incomes