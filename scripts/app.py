from flask import Flask, request, jsonify
from flask_cors import CORS
from sudoku import solve
from scrape import scrape
from flask_graphql import GraphQLView
# from flask_sockets import FlaskWebSocket
import graphene
import uuid
import json
from flask_sqlalchemy import SQLAlchemy
import config
from user import register, login, removeUser, fav, getFav, removeFav
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy.dialects.postgresql import ARRAY

def generate_execution_id():
    # Generate a UUID as the execution ID
    return str(uuid.uuid4())

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
cors = CORS(app)
db = SQLAlchemy(app)

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
    sudoku = db.Column(ARRAY(db.Integer))
    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'))

    def __init__(self, sudoku, user_id):
        self.sudoku = sudoku
        self.user_id = user_id
 
    def __repr__(self):
        return 'Sudoku number {sudokuId} is {sudoku}.'.format(sudokuId = self.id, sudoku = self.sudoku)

class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User

class SudokuObject(SQLAlchemyObjectType):
    class Meta:
        model = Sudoku

#sockets = FlaskWebSocket(app)

'''
# Flask RESTful APIs
@app.route("/solve", methods=["POST"])
def postSolve():
    data = request.get_json()
    result = solve(data['sudoku'], data['size'])
    data = {
        "headers": {'Content-Type':'application/json',
                    "Access-Control-Allow-Headers" : "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"},
        "body": result,
        "statusCode": 200,
    }
    return jsonify(data)

@app.route("/scrape", methods=["POST"])
def postScrape():
    data = request.get_json()
    scrapedData = scrape(data['index'], data['difficulty'])
    data = {
        "headers": {'Content-Type':'application/json',
                    "Access-Control-Allow-Headers" : "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"},
        "body": scrapedData,
        "statusCode": 200,
    }
    return jsonify(data)
'''
class SudokuOutput(graphene.ObjectType):
    arr = graphene.List(graphene.Int)

class Message(graphene.ObjectType):
    text = graphene.String()

class SolveSudoku(graphene.Mutation):
    class Arguments:
        sudoku = graphene.List(graphene.Int, required=True)
        size = graphene.Int(required = True)

    execution_id = graphene.String()
    solution = graphene.List(graphene.Int, required = True)
    time = graphene.Float(required = True)

    def mutate(root, info, sudoku, size):
        # Generate a unique execution ID
        execution_id = generate_execution_id()

        # Emit subscription event indicating the start of the function execution
        # sockets.emit('function_update', {'execution_id': execution_id, 'text': 'Solving...'})

        # Call solve() function, passing the arguments
        solved_sudoku = solve(sudoku, size)

        # Emit subscription event indicating the function is finished
        # sockets.emit('function_update', {'execution_id': execution_id, 'text': 'Finished.'})

        # Convert the solved puzzle to a plain list of integers
        return SolveSudoku(
            execution_id=execution_id,
            solution = solved_sudoku['solution'],
            time = solved_sudoku['time']
        )

class ScrapeSudoku(graphene.Mutation):
    class Arguments:
        index = graphene.Int(required = True)
        difficulty = graphene.String(required = False)

    execution_id = graphene.String()
    sudoku = graphene.List(graphene.Int, required = True)
    size = graphene.Int(required = True)
    difficulty = graphene.String(required = False)

    def mutate(root, info, index, difficulty = ''):
         # Generate a unique execution ID
        execution_id = generate_execution_id()

        # Emit subscription event indicating the start of the function execution
        # sockets.emit('function_update', {'execution_id': execution_id, 'text': 'Retrieving...'})

        # Call scrape() function passing the arguments
        scraped_sudoku = scrape(index, difficulty)

        # Convert the solved puzzle to a plain list of integers
        if 'difficulty' in scraped_sudoku:
            result = ScrapeSudoku(
                execution_id=execution_id,
                sudoku=scraped_sudoku['sudoku'],
                size=scraped_sudoku['size'],
                difficulty=scraped_sudoku['difficulty']
            )
        else:
            result = ScrapeSudoku(
                execution_id=execution_id,
                sudoku=scraped_sudoku['sudoku'],
                size=scraped_sudoku['size'],
                difficulty=''
            )

        # Emit subscription event indicating the function is finished
        # sockets.emit('function_update', {'execution_id': execution_id, 'text': 'Finished.'})

        return result

class Register(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        name = graphene.String(required=True)

    user = graphene.Field(UserObject)  # Assuming you have defined the User type in your schema

    def mutate(self, info, email, password, name):
        # Check if email already exists
        if User.query.filter_by(email=email).first():
            return None  # Email already exists, return None or raise an exception

        new_user = register(db, Sudoku, User, email = email, password = password, name = name)
        return Register(user = new_user)

class Login(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(UserObject)  # Assuming you have defined the User type in your schema

    def mutate(self, info, email, password):
        user = login(db, Sudoku, User, email = email, password = password)
        return Login(user = user)
    
class RemoveUser(graphene.Mutation):
    class Arguments:
        userId = graphene.Int(required=True)

    success = graphene.Boolean()  # Assuming you have defined the User type in your schema

    def mutate(self, info, user_id):
        success = removeUser(db, Sudoku, User, user_id = user_id)
        return RemoveUser(success = success)

class Fav(graphene.Mutation):
    class Arguments:
        sudoku = graphene.List(graphene.Int, required=True)
        user_id = graphene.Int(required=True)

    success = graphene.Boolean()  # Assuming you have defined the User type in your schema

    def mutate(self, info, sudoku, user_id):
        success = fav(db, Sudoku, User, sudoku = sudoku, user_id = user_id)
        return Fav(success = success)
        

class GetFav(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int(required=True)

    fav_sudokus = graphene.List(SudokuObject, required=False)  # Assuming you have defined the User type in your schema

    def mutate(self, info, user_id):
        fav_sudokus = getFav(db, Sudoku, User, user_id = user_id)
        if fav_sudokus is not None:
            return GetFav(fav_sudokus = fav_sudokus)
            # Empty list or list with elements
        else:
            return GetFav(fav_sudokus = None)
            # User does not exist

class RemoveFav(graphene.Mutation):
    class Arguments:
        sudoku_id = graphene.Int(required=True)
        user_id = graphene.Int(required=True)

    success = graphene.Boolean()  # Assuming you have defined the User type in your schema

    def mutate(self, info, sudoku_id, user_id):
        success = removeFav(db, Sudoku, User, sudoku_id = sudoku_id, user_id = user_id)
        return RemoveFav(success = success)
            
'''
class Query(graphene.ObjectType):
    # Add any necessary query fields here
    pass
'''

class Mutation(graphene.ObjectType):
    solve_sudoku = SolveSudoku.Field()
    scrape_sudoku = ScrapeSudoku.Field()
    register = Register.Field()
    login = Login.Field()
    remove_user = RemoveUser.Field()
    fav = Fav.Field()
    get_fav = GetFav.Field()
    remove_fav = RemoveFav.Field()

'''
class Subscription(graphene.ObjectType):
    function_update = graphene.Field(Message, execution_id=graphene.String())

    def resolve_function_update(root, info, execution_id):
        # Subscribe to the function_update event based on the execution_id
        # Return the execution updates for the specified execution_id
        return Message(text='Function updates.')
'''
schema = graphene.Schema(
    #query = Query, 
    mutation = Mutation
    #subscription = Subscription
)
'''
class FunctionUpdateWebSocket(FlaskWebSocket):
    def on_message(self, message):
        data = json.loads(message)
        event = data.get('event')
        execution_id = data.get('execution_id')

        if event == 'subscribe':
            # Join the room based on the execution_id
            self.join_room(execution_id)
            sockets.emit('function_update', {'execution_id': execution_id, 'text': 'Subscribed'}, room=execution_id)
        elif event == 'unsubscribe':
            # Leave the room based on the execution_id
            self.leave_room(execution_id)
            sockets.emit('function_update', {'execution_id': execution_id, 'text': 'Unsubscribed'}, room=execution_id)

sockets.register_blueprint(FunctionUpdateWebSocket, url_prefix='/')
'''
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql', 
        schema=schema, 
        graphiql=True)
)

if __name__ == '__main__':
    app.run(debug=True)