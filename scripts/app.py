from flask import Flask, request, jsonify
from flask_cors import CORS
from sudoku import solve
from scrape import scrape
from flask_graphql import GraphQLView
import graphene

app = Flask(__name__)
cors = CORS(app)

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

class Mutation(graphene.ObjectType):
    solve_sudoku = SolveSudoku.Field()
    scrape_sudoku = ScrapeSudoku.Field()

'''
class Query(graphene.ObjectType):
    # Add any necessary query fields here
    pass
'''

schema = graphene.Schema(
    #query=Query, 
    mutation=Mutation
)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql', 
        schema=schema, 
        graphiql=True)
)

if __name__ == '__main__':
    app.run(debug=True)

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