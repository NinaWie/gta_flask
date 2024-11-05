import numpy as np

import pyproj

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin  # needs to be installed via pip install flask-cors

from backend import get_mean_value_from_table

def new_func():
    print("hoi")

new_func()

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


@app.route("/round_float", methods=["GET"])
def round_float():
    input_value = float(request.args.get("num", 1))
    print(f"Received argument: {input_value}")
    new_value = round(input_value,2)
    return jsonify({"output": new_value})

# TODO: TASK 2
@app.route("/project_coords", methods=["POST"])
@cross_origin()
def project_coords():
    coords =  request.get_json(force=True)
    print(coords)
    transformer = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:2056")
    projected_x, projected_y = transformer.transform(coords[0], coords[1])
    projected_coords = [projected_x, projected_y]
    
    return jsonify(projected_coords)


@app.route("/project_coords", methods=["POST"])
def project_coords():
    coords = request.get_json(force=True)
    print("received:", coords)
    lat, lon = coords
    print("lat, lon are", lat, lon, "of type", type(lat), type(lon))
    new_coords = pyproj.transform(4326, 2056, lat, lon)
    print("converted to:", new_coords)
    return jsonify({"output": new_coords})

# TODO TASK 3
@app.route("/project_to_crs", methods=["POST"])
def project_to_crs():
    coords = request.get_json(force=True)
    print("received:", coords)
    crs, lat, lon = coords
    new_coords = pyproj.transform(4326, crs, lat, lon)
    print("converted to:", new_coords)
    return jsonify({"output": new_coords})

@app.route("/project_coords_extended", methods=["GET","POST"])
@cross_origin()
def project_coords_extended():
    coords =  request.get_json(force=True)
    crs = request.args.get("crs", 4326)
    transformer = pyproj.Transformer.from_crs("EPSG:4326", f"EPSG:{crs}")
    projected_x, projected_y = transformer.transform(coords[0], coords[1])
    projected_coords = [projected_x, projected_y]
    
    return jsonify(projected_coords)


@app.route('/increase_value', methods=['GET'])
def increase_value():
    # Get the current value from the request arguments and increase it
    current_value = int(request.args.get('value', 0))
    new_value = current_value + 1
    response = jsonify({"value": new_value})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/decrease_value', methods=['GET'])
def decrease_value():
    # Get the current value from the request arguments and decrease it
    current_value = int(request.args.get('value', 0))
    new_value = current_value - 1
    response = jsonify({"value": new_value})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response




# TODO TASK 5
@app.route("/compute_mean", methods=["GET"])
def compute_mean():
    # retrieve column name from the request arguments
    col_name = str(request.args.get("column_name", "value"))

    # call backend
    result = get_mean_value_from_table(col_name)

    # save results in a suitable format to output
    result = jsonify({"mean": result})
    return result


if __name__ == "__main__":
    # run
    app.run(debug=True, host="localhost", port=8989)
