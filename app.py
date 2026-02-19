from flask import Flask, request, current_app, jsonify

app = Flask(__name__)

@app.before_request
def log_request_info():
    print(f"Method: {request.method} | Path: {request.path}")

@app.after_request
def add_custom_header(response):
    response.headers["X-Custom-Header"] = "FlaskRocks"
    return response

@app.teardown_request
def log_teardown_exception(exception):
    if exception:
        print(f"Teardown caught exception: {exception}")

@app.route("/")
def hello_world():
    print(request)
    return "<h1>Welcome to My Flask API!</h1>"

@app.route("/about")
def about():
    print(request)
    return {"name": "Your Name", "course": "MCON-504 - Backend Development", "semester": "Spring 2025"}

@app.route("/greet/<name>")
def greet(name):
    print(request)
    return f"<p>Hello, {name}! Welcome to Flask.</p>"

@app.route("/calculate")
def calculate():
    print(request)
    queryparams = request.args.to_dict()
    print(queryparams)
    try:
        num1 = int(queryparams["num1"])
        num2 = int(queryparams["num2"])
        operation = queryparams["operation"]
        result = None
        if operation == "add":
            result = num1 + num2
        if operation == "subtract":
            result = num1 - num2
        if operation == "multiply":
            result = num1 * num2
        if operation == "divide":
            result = num1 / num2

        return jsonify({"result": result, "operation": operation})

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred during calculation"}), 500

@app.route("/echo", methods=["POST"])
def echo():
    print(request)
    recieved = request.get_json()
    print(recieved)
    response = {**recieved, "echoed": True}
    return jsonify(response)
###{"message": "Hello", "echoed": true}

@app.route("/status/<int:code>", methods=["GET"])
def status_code_practice(code):
    return f"This is a {code} error", code


if __name__ == "__main__":
    app.run(debug=True)