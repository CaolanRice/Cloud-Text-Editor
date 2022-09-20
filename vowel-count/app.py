from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)


class vowelCount(Resource):

    def get(self):
        text = request.args['text']

        status = 200
        result = 0

        # if theres no text return bad request error
        if len(text) == 0:
            status = 400
        else:
            result = vowel_count(text)

        data = {
            'status': status,
            'string': 'Contains ' + str(result) + ' vowels',
            'result': result
        }

        return jsonify(data)


def vowel_count(text):

    text = text.lower()
    counter = 0

    for character in text:
        if character in 'aeiou':
            counter += 1

    return counter


api.add_resource(vowelCount, "/")

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
