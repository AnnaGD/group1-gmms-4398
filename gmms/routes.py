from gmms import app
from flask import render_template

#@app.route('/')
#def hello():
#    return "Hello World!"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/customer')
def Customer():
    return render_template("customer.html")

@app.route('/technician')
def Technician():
    return render_template("technician.html")

@app.route('/approver')
def Approver():
    return render_template("approver.html")