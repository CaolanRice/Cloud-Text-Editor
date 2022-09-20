from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)

class palindromeCount(Resource):

    def get(self):
        text = request.args['text']

        status = 200
        result = 0

        if len(text) == 0:
            status = 400
        else:
            result = palindrome_count(text.lower())

        data={
            'status': status,
            'string': 'Contains ' + str(result) + ' palindromes',
            'result': result
        }

        return jsonify(data)


def palindrome_count(text):

    text = text
    counter = 0

    for word in text.split(" "):
        if word==word[::-1]:
            counter += 1

    return counter 



api.add_resource(palindromeCount, "/")

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")




