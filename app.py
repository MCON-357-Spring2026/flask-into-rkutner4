from flask import Flask, request, current_app, jsonify

app = Flask(__name__)

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
    return f"{result}"

@app.route("/echo", methods=["POST"])
def echo():
    print(request)
    recieved = request.get_json
    print(recieved)
    response = {**recieved, "echoed": True}
    return jsonify(response)
###{"message": "Hello", "echoed": true}

@app.route("/status/<int:code>", methods=["GET"])
def status_code_practice(code):
    return f"This is a {code} error", code


if __name__ == "__main__":
    app.run(debug=True)