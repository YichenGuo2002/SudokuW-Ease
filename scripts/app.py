from flask import Flask, request, jsonify
from flask_cors import CORS
from sudoku import solve
from scrape import scrape
from flask_graphql import GraphQLView
from flask_sockets import Sockets
from flask_socketio import SocketIO, emit, join_room, leave_room
import graphene
import uuid
import json

def generate_execution_id():
    # Generate a UUID as the execution ID
    return str(uuid.uuid4())

app = Flask(__name__)
cors = CORS(app)
socketio = SocketIO(app)
sockets = Sockets(app)

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

class Sudoku(graphene.ObjectType):
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
        emit('function_update', {'execution_id': execution_id, 'text': 'Solving...'})

        # Call solve() function, passing the arguments
        solved_sudoku = solve(sudoku, size)

        # Emit subscription event indicating the function is finished
        emit('function_update', {'execution_id': execution_id, 'text': 'Finished.'})

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
        emit('function_update', {'execution_id': execution_id, 'text': 'Retrieving...'})

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
        emit('function_update', {'execution_id': execution_id, 'text': 'Finished.'})

        return result
        
'''
class Query(graphene.ObjectType):
    # Add any necessary query fields here
    pass
'''

class Mutation(graphene.ObjectType):
    solve_sudoku = SolveSudoku.Field()
    scrape_sudoku = ScrapeSudoku.Field()

class Subscription(graphene.ObjectType):
    function_update = graphene.Field(Message, execution_id=graphene.String())

    def resolve_function_update(root, info, execution_id):
        # Subscribe to the function_update event based on the execution_id
        # Return the execution updates for the specified execution_id
        return Message(text='Function updates.')

schema = graphene.Schema(
    #query = Query, 
    mutation = Mutation,
    subscription = Subscription
)

@sockets.route('/graphql')
def handle_websocket(sock):
    while not sock.closed:
        message = sock.receive()
        if message:
            # Parse the incoming WebSocket message
            data = json.loads(message)
            event = data.get('event')
            execution_id = data.get('execution_id')

            if event == 'subscribe':
                # Join the room based on the execution_id
                join_room(execution_id)
                emit('function_update', {'execution_id': execution_id, 'text': 'Subscribed'}, room=execution_id)
            elif event == 'unsubscribe':
                # Leave the room based on the execution_id
                leave_room(execution_id)
                emit('function_update', {'execution_id': execution_id, 'text': 'Unsubscribed'}, room=execution_id)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql', 
        schema=schema, 
        graphiql=True)
)

if __name__ == '__main__':
    socketio.run(app
    # , host='0.0.0.0'
                 )
'''
Sample request query: 
mutation SolveSudoku{
  solveSudoku(
		sudoku: [0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0],
		size: 9
	) 
	{
   solution,
	 time
  }
}

mutation ScrapeSudoku{
  scrapeSudoku(
		index: 6
	) 
	{
   sudoku,
		size,
		difficulty
  }
}

'''