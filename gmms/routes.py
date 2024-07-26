from gmms import app
from flask import render_template

#@app.route('/')
#def hello():
#    return "Hello World!"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/customer', methods=["POST", "GET"])
def Customer():
    username = None
    if "customer" in session:
        customer = session["customer"]

        if request.method == "POST":
            username = request.form["username"]
            session["username"] = username
        else:
            if "username" in session:
                username = session["username"]

        return render_template("customer.html", username=username)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route('/technician')
def Technician():
    return render_template("technician.html")

@app.route('/approver')
def Approver():
    return render_template("approver.html")

@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("customer", None)
    session.pop("username", None) #user logged out
    return redirect(url_for("index"))
