from app import db

class User(db.Model):
    __tablename__ = 'user_table'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(60))
    password = db.Column(db.String(24))
    name = db.Column(db.String(24))
    fav = db.relationship('Sudoku', backref='user')

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name
        self.fav = []
 
    def __repr__(self):
        return 'User number {userId} with email {email}.'.format(userId = self.id, email = self.email)
    
    def add_fav(self, sudoku):
        self.fav.append(sudoku)
        db.session.commit()

class Sudoku(db.Model):
    __tablename__ = 'sudoku_table'

    id = db.Column(db.Integer, primary_key = True)
    sudoku = db.Column(db.ARRAY(db.Integer))
    userId = db.Column(db.Integer, db.ForeignKey('user_table.id'))

    def __init__(self, sudoku, userId):
        self.sudoku = sudoku
        self.userId = userId
 
    def __repr__(self):
        return 'Sudoku number {sudokuId} is {sudoku}.'.format(sudokuId = self.userId, sudoku = self.sudoku)

