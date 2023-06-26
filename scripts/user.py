#from model import db

'''
## Email restrictions: 
Allowed characters:
latin letters (a-z).
numbers (0-9).
special characters: underscores (_), periods (.), and dashes (-).
A period (.) is not permitted at the start or end.
Consecutive periods or special characters (e.g., john…doe@company.com) are not allowed.
Special characters should be followed by one or more letters or numbers.
Must include an at sign (@).

## Password restrictions:
Minimum password length >= 6
Maximum password length <= 24
Require at least one lowercase letter
Require at least one uppercase letter
Require at least one number
Require at least one of the following characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

## Name restrictions:
Allowed characters:
latin letters (a-z).
numbers (0-9).
special characters: underscores (_), periods (.), and dashes (-). 
Usernames cannot contain an ampersand (&), equals sign (=), apostrophe ('), dash (-), plus sign (+), comma (,), brackets (<,>), or more than one period (.) in a row.
Maximum username length <= 24
'''
def register(email, password, name):
    pass

def login(email, password):
    pass

def removeUser(userId):
    pass

'''
## Sudoku restrictions:
Array length is one of 16, 81, 256, and 625.
'''
def fav(sudoku, userId):
    pass

def getFav(userId):
    pass

def removeFav(sudokuId, userId):
    pass