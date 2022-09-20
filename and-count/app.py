from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)


class andCount(Resource):

    def get(self):
        text = request.args['text']

        status = 200
        result = 0

        # if theres no text return bad request error
        if len(text) == 0:
            status = 400
        else:
            result = and_count(text)

        data = {
            'status': status,
            'string': 'Contains ' + str(result) + ' ands',
            'result': result
        }

        return jsonify(data)


# method to
def and_count(text):

    text = text.lower()
    split_text = text.split(' ')
    counter = 0

    for word in split_text:
        if word == 'and':
            counter += 1

    return counter


api.add_resource(andCount, "/")

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
