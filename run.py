from flask import Flask, render_template, request
app = Flask(__name__)

class Item:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


@app.route("/")
def hello_world():

    # items = [
    #     Item("Apple", 10),
    #     Item("Pear", 5),
    #     Item("Banana", 30)
    # ]

    items = [
        {"name":"Apple", "amount": 10},
        {"name": "Pear", "amount": 5},
        {"name": "Banana", "amount": 10}
    ]
    output = render_template("start.html", name="John Doe", items=items)
    print(output)
    return output


@app.route("/test")
def hello_name():
    args = request.args
    name = args.get("name")
    age = args.get("age")
    return render_template("test.html", name=name, age=age)