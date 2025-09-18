from flask import Flask, render_template, request

app = Flask(__name__) # take variable name as app by convention; The function call turns file as a flask app

@app.route('/') #decorator; the default page
def index(): # the function name can be anything, just name it as index()
    return  render_template("index.html") # index.html, but we can't return it directly

@app.route('/greet')
def greet():
    return render_template("greet.html", name=request.args.get('name', 'world'))