from flask import Flask, request, jsonify
from flask_cors import CORS
from sudoku import solve
from scrape import scrape
from flask_graphql import GraphQLView
from flask_sockets import Sockets
from flask_socketio import SocketIO, emit
import graphene

app = Flask(__name__)
cors = CORS(app)
socketio = SocketIO(app)

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

    solution = graphene.List(graphene.Int, required = True)
    time = graphene.Float(required = True)

    def mutate(root, info, sudoku, size):
        # Call solve() function passing the
        solved_sudoku = solve(sudoku, size)

        # Convert the solved puzzle to a plain list of integers
        return SolveSudoku(
            solution = solved_sudoku['solution'],
            time = solved_sudoku['time']
        )

class ScrapeSudoku(graphene.Mutation):
    class Arguments:
        index = graphene.Int(required = True)
        difficulty = graphene.String(required = False)

    sudoku = graphene.List(graphene.Int, required = True)
    size = graphene.Int(required = True)
    difficulty = graphene.String(required = False)

    def mutate(root, info, index, difficulty = ''):
        # Call scrape() function passing the
        scraped_sudoku = scrape(index, difficulty)

        # Convert the solved puzzle to a plain list of integers
        if 'difficulty' in scraped_sudoku:
            return ScrapeSudoku(
                sudoku = scraped_sudoku['sudoku'],
                size = scraped_sudoku['size'],
                difficulty = scraped_sudoku['difficulty']
            )
        else:
            return ScrapeSudoku(
                sudoku = scraped_sudoku['sudoku'],
                size = scraped_sudoku['size'],
                difficulty = ''
            )
        
'''
class Query(graphene.ObjectType):
    # Add any necessary query fields here
    pass
'''

class Mutation(graphene.ObjectType):
    solve_sudoku = SolveSudoku.Field()
    scrape_sudoku = ScrapeSudoku.Field()

class Subscription(graphene.ObjectType):
    new_message = graphene.Field(Message)

    def resolve_new_message(root, info):
        # Implement your resolver logic here
        return [...]

schema = graphene.Schema(
    #query = Query, 
    mutation = Mutation,
    subscription = Subscription
)

@socketio.on('subscribe')
def handle_subscribe(subscription_params):
    subscription = subscription_params.get('subscription')
    # Implement your subscription logic here
    # Use 'emit' to send updates to subscribed clients

@socketio.on('unsubscribe')
def handle_unsubscribe(subscription_params):
    subscription = subscription_params.get('subscription')
    # Implement your unsubscription logic here

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