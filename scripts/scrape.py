import requests
from bs4 import BeautifulSoup
import re
import json

def translateToArray(digits):
    result = []
    for digit in digits:
        if(digit in "."):
            result.append(0)
        elif(digit in '0123456789'):
            result.append(int(digit))
    return result

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

def retrieveArto2006():
    return [8, 5, 0, 0, 0, 2, 4, 0, 0, 7, 2, 0, 0, 0, 0, 0, 0, 9, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 7, 0, 0, 2, 3, 0, 5, 0, 0, 0, 9, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 7, 0, 0, 1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 6, 0, 4, 0]

def retrieveArto2010():
    return [0, 0, 5, 3, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 2, 0, 0, 7, 0, 0, 1, 0, 5, 0, 0, 4, 0, 0, 0, 0, 5, 3, 0, 0, 0, 1, 0, 0, 7, 0, 0, 0, 6, 0, 0, 3, 2, 0, 0, 0, 8, 0, 0, 6, 0, 5, 0, 0, 0, 0, 9, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 9, 7, 0, 0]

def retrieveWPC2020():
    return translateToArray('...5.7.....24.63...9..1..2.27.....68..3...1..14.....93.6..4..5...92.56.....9.3...')

def retrieveWPC2020Advanced():
    return translateToArray('...8.9.....5...7...29.1.64.7...6...2..62.43..8...7...6.37.2.81...1...5.....1.3...')

def retrieveSlowestPeter():
    return translateToArray('.....6....59.....82....8....45........3........6..3.54...325..6..................')

def retrieveImpossiblePeter():
    return translateToArray(
    '''. . . |. . 5 |. 8 . 
    . . . |6 . 1 |. 4 3 
    . . . |. . . |. . . 
    ------+------+------
    . 1 . |5 . . |. . . 
    . . . |1 . 6 |. . . 
    3 . . |. . . |. . 5 
    ------+------+------
    5 3 . |. . . |. 6 1 
    . . . |. . . |. . 4 
    . . . |. . . |. . . ''')