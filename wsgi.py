from flask import Flask, request, current_app

app = Flask(__name__)

@app.route("/")
def hello_world():
    print(request)
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)