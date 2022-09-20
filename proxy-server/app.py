from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from dotenv import load_dotenv
import requests
import os

load_dotenv()


app = Flask(__name__)
CORS(app)
api = Api(app)


class proxyServer(Resource):

    def get(self):

        service = request.args["service"].upper()
        text = request.args["text"]

        if service is None or text is None:
            payload = {
                "result": 0,
                "status": 400,
                "string": ""
            }
            return jsonify(payload)

        # get all keys from env and append them to a new list
        # if the service requested is listed within the new list
        # then make the request otherwise return error payload

        services = []
        for k, _ in os.environ.items():
            services.append(k)

        # check if service exists
        if service in services:
            r = requests.get(os.getenv(service) + "?text=" + text)
            resp = r.json()

            # reformat response from comma_count function
            if service == "COMMA_COUNT":
                resp = {
                    "result": resp["Count"],
                    "status": resp["Status"],
                    "string": resp["String"]
                }

            return jsonify(resp)

        # bad request - unknown service requested
        payload = {
            "result": 0,
            "status": 404,
            "string": ""

        }
        return jsonify(payload)


api.add_resource(proxyServer, "/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
