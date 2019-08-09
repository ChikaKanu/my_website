from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    items = ["Apple", "Pear", "Banana"]
    output = ""
    for fruit in items:
        output += "<h3>" + fruit + "</h3>"
    return output

@app.route("/name")
def hello_name():
    paragraph = "<p>You are here</p>"
    return "Chika kanu is my name" + paragraph