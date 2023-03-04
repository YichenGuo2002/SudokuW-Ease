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



print(scrapeNYTimes())