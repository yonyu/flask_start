from flask import Flask, render_template, request

app = Flask(__name__) # take variable name as app by convention; The function call turns file as a flask app

@app.route('/', methods=["GET", "POST"]) #decorator; the default page
def index(): # the function name can be anything, just name it as index()
    if request.method == "GET":
        return  render_template("index.html") # index.html, but we can't return it directly
    elif request.method == "POST":
        return render_template("greet.html", name=request.form.get('name', 'world'))