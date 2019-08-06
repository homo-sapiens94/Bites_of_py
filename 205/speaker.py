from urllib.request import urlretrieve
from pathlib import Path

import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup

TMP = Path('/tmp')
PYCON_HTML = TMP / "pycon2019.html"
if not PYCON_HTML.exists():
    urlretrieve('https://bit.ly/2O5Bik7', PYCON_HTML)


def _get_soup(html=PYCON_HTML):
    return Soup(html.read_text(), "html.parser")


def get_pycon_speaker_first_names(soup=None):
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    soup = _get_soup()
    spans = soup.findAll('span', attrs = {'class':'speaker'}) 
    lines = [span.get_text().strip() for span in spans]
    
    all_full_names=[]
    for name in lines:
        names = name.replace(',','#').replace('/','#').split('#')
        for full in names:
            all_full_names.append(full)

    all_first_names=[]
    for name in all_full_names:
      name = name.split()[0]
      all_first_names.append(name)
    
    return all_first_names


def get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers, rounded to 2 decimal places."""
    female_name=[]
    d = gender.Detector()
    for name in first_names:
      morf = d.get_gender(name)
      if morf=='female' or morf=='mostly_female':
        female_name.append(name)
    
    percentage = round(((len(female_name)/len(first_names))*100),2)
    return percentage
if __name__ == '__main__':
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)




#pybites solution




from urllib.request import urlretrieve
from pathlib import Path
import re

import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup

TMP = Path('/tmp')
PYCON_HTML = TMP / "pycon2019.html"
if not PYCON_HTML.exists():
    urlretrieve('https://bit.ly/2O5Bik7', PYCON_HTML)


def _get_soup(html=PYCON_HTML):
    return Soup(html.read_text(), "html.parser")


def _extract_names(names):
    for name in names:
        extracted_names = re.split(r'[,/]', name)
        for en in extracted_names:
            yield en.strip()


def _get_first_names(names):
    return [n.split()[0] for n in names]


def get_pycon_speaker_first_names(soup=None):
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    if soup is None:
        soup = _get_soup()

    speakers = soup.find_all("span", {"class": "speaker"})
    names = [speaker.text.strip() for speaker in speakers]

    names = list(_extract_names(names))
    return _get_first_names(names)


def get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers, rounded to 2 decimal places."""
    d = gender.Detector()
    num_females = 0

    for name in first_names:
        gg = d.get_gender(name)
        if 'female' in gg:
            num_females += 1

    return round(num_females/len(first_names) * 100, 2)


if __name__ == '__main__':
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)