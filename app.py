from flask import Flask, render_template, request

app = Flask(__name__) # use app as name by convention; turn file as flask app

@app.route('/') #decorator; the default page
def index(): # the function name can be anything, just name it as index

    name = request.args.get("name", "world") # get the name from the url
    
    return  render_template("index.html", name = name) # index.html, but we can't return it directly