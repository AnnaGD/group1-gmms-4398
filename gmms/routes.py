from gmms import app

@app.route('/')
def hello():
    return "Hello World!"