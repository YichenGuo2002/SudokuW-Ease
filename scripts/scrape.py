import requests
from bs4 import BeautifulSoup
import re
import json

def scrapeNYTimes():
    URL = "https://www.nytimes.com/puzzles/sudoku/hard"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    scripts = soup.find('script', string=re.compile('window.gameData')).text
    data = scripts.split("=", 1)[1]
    ld = json.loads(data)
    return{
        'easy':ld['easy']['puzzle_data']['puzzle'],
        'medium':ld['medium']['puzzle_data']['puzzle'],
        'hard':ld['hard']['puzzle_data']['puzzle']
    } 

# https://menneske.no/
def scrapeMenneskeNo():
    URL = 'https://menneske.no/sudoku/eng/random.html'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    scripts = soup.find('div', {'class':re.compile('grid')})
    tds = scripts.find_all('td')
    result = []
    for td in tds:
        if(td.text != '\xa0'):
            result.append(int(td.text))
        else:
            result.append(0)
    return result

# https://www.sudokuweb.org/
def scrapeSudokuWebOrg():
    URL = 'https://www.sudokuweb.org/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    scripts = soup.find('table')
    spans = scripts.find_all('span')
    result = []
    for span in spans:
        if(span['class'][0] == "sedy"):
            result.append(int(span.text))
        elif(span['class'][0] == 'vloz'):
            result.append(0)
    return result

# https://www.sudoku.org.uk/daily.asp
def scrapeSudokuOrgUK():
    URL = 'https://www.sudoku.org.uk/daily.asp'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    tds = soup.find_all('td', {'class':re.compile('InnerTDone')})
    result = []
    for td in tds:
        if(td.text):
            result.append(int(td.text))
        else:
            result.append(0)
    return result



print(scrape())