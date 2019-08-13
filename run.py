from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello_world():
    items = ["Apple", "Pear", "Banana"]
    output = render_template("start.html", name="John Doe", items=items)
    print (output)
    return output


@app.route("/test")
def hello_name():
    return render_template("test.html", name="John Doe")