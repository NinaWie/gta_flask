import numpy as np

import pyproj

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin  # needs to be installed via pip install flask-cors

from backend import get_mean_value_from_table

app = Flask(__name__)
CORS(app, origins=["*", "null"])  # allowing any origin as well as localhost (null)


@app.route("/welcome_to_flask", methods=["GET"])
def welcome_to_flask():
    print("all good")
    return jsonify("Welcome!")


@app.route("/arguments", methods=["GET"])
def working_with_arguments():
    my_argument = str(request.args.get("name", "default_name"))

    return jsonify(f"This is how we pass arguments in GET request. My name is {my_argument}")


@app.route("/add_numbers", methods=["GET"])
def add_numbers():
    try:
        input_value_1 = int(request.args.get("num1", 1))
    except ValueError:
        return jsonify("Invalid input for num1")
    print(f"Received argument 1: {input_value_1}")
    input_value_2 = int(request.args.get("num2", 2))
    print(f"Received argument 2: {input_value_2}")
    new_value = input_value_1 + input_value_2
    return jsonify({"output": new_value})


@app.route("/access_with_javascript", methods=["GET"])
@cross_origin()
def javascript_demo():
    """method to demonstrate how to access this endpoint with javascript"""
    response = jsonify("This should be shown on your website")
    return response


@app.route("/using_post", methods=["POST"])
@cross_origin()
def using_post():
    user_profile = request.get_json(force=True)
    print(user_profile)
    output_text = f"The app received data from user {user_profile['username']} and password {user_profile['password']}"
    return jsonify(output_text)


# TODO: TASK 1
# @app.route("/round_float", methods=["GET"])
# def round_float():
#     ...

# TODO: TASK 2

# TODO TASK 3

# TODO TASK 4


# TODO TASK 5
@app.route("/compute_mean", methods=["GET"])
def compute_mean():
    # retrieve column name from the request arguments
    # TODO

    # call backend
    # TODO

    # return results (mean value) as a json
    # TODO
    pass


if __name__ == "__main__":
    # run
    app.run(debug=True, host="localhost", port=8989)
