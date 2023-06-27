#from model import db

'''
## Email restrictions: 
Maximum email length <= 60
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
def register(db, Sudoku, User, email, password, name):
      # Check if email already exists
    if User.query.filter_by(email=email).first():
        return None  # Email already exists, return None or raise an exception

    new_user = User(email=email, password=password, name=name)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def login(db, Sudoku, User, email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        return user
    else:
        return None

def removeUser(db, Sudoku, User, userId):
    user = User.query.get(userId)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    else:
        return False
    
'''
## Sudoku restrictions:
Array length is one of 16, 81, 256, and 625.
'''
def fav(db, Sudoku, User, sudoku, userId):
    # Create a new Sudoku instance
    new_sudoku = Sudoku(sudoku=sudoku, userId=userId)
    db.session.add(new_sudoku)
    db.session.commit()

    # Retrieve the corresponding user
    user = User.query.get(userId)

    # Add the Sudoku's ID to the user's favorite list
    user.add_fav(new_sudoku)

def getFav(db, Sudoku, User, userId):
    # Retrieve the user object with the provided userId
    user = User.query.get(userId)

    if user:
        # Retrieve the user's favorite list of Sudokus
        fav_list = user.fav

        # Retrieve the Sudoku data for each Sudoku ID in the favorite list
        fav_sudokus = []
        for sudoku in fav_list:
            fav_sudoku = Sudoku.query.get(sudoku.id)
            fav_sudokus.append(fav_sudoku)
        return fav_sudokus
    else:
        return None

def removeFav(db, Sudoku, User, sudokuId, userId):
       # Retrieve the user object with the provided userId
    user = User.query.get(userId)

    if user:
        # Retrieve the Sudoku object with the provided sudokuId
        sudoku = Sudoku.query.get(sudokuId)

        if sudoku:
            # Remove the Sudoku from the user's favorite list
            user.fav.remove(sudoku)
            db.session.commit()
            return True
        else:
            return False
    else:
        return False