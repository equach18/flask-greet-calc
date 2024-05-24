# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route("/add")
def to_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a,b))

@app.route("/sub")
def to_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a,b))

@app.route("/mult")
def to_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a,b))

@app.route("/div")
def to_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a,b))

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.route("/math/<operation>")
def to_math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(operators[operation](a,b))