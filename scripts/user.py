#from model import db
from sqlalchemy.dialects.postgresql import ARRAY


'''
## Email restrictions: 
Maximum email length <= 60
Allowed characters:
latin letters (a-z).
numbers (0-9).
special characters: underscores (_), periods (.), and dashes (-).
Must include an at sign (@).

## Password restrictions:
Minimum password length >= 6
Maximum password length <= 24
Require at least one lowercase letter
Require at least one uppercase letter
Require at least one number

## Name restrictions:
Allowed characters:
latin letters (a-z).
numbers (0-9).
special characters: underscores (_), periods (.), and dashes (-). 
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

def removeUser(db, Sudoku, User, user_id):
    user = User.query.get(user_id)
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
def fav(db, Sudoku, User, sudoku, user_id):
    try:
        # Create a new Sudoku instance
        new_sudoku = Sudoku(sudoku = sudoku, user_id = user_id)
        db.session.add(new_sudoku)
        db.session.commit()

       # Retrieve the corresponding user
        user = User.query.get(user_id)
        # Add the Sudoku's ID to the user's favorite list
        user.add_fav(new_sudoku)
        db.session.commit()
        return True
    except Exception as err:
        print(err)
        return False

def getFav(db, Sudoku, User, user_id):
    # Retrieve the user object with the provided userId
    user = User.query.get(user_id)

    if user:
        # Retrieve the user's favorite list of Sudokus
        fav_list = user.fav

        return fav_list
    else:
        return None

def removeFav(db, Sudoku, User, sudoku_id, user_id):
       # Retrieve the user object with the provided userId
    user = User.query.get(user_id)

    if user:
        # Retrieve the Sudoku object with the provided sudokuId
        sudoku = Sudoku.query.get(sudoku_id)

        if sudoku and sudoku.user_id == user_id:
            # Remove the Sudoku from the user's favorite list
            user.fav.remove(sudoku)
            db.session.commit()
            return True
        else:
            return False
    else:
        return False