# imports
from flask import Flask

# zmienna aplikacji
app = Flask(__name__)

# routing
@app.route('/')
def hello_world():
    return '<h1>Flask jest spoko!</h1>'

# debug
if __name__=='__main__':
	app.run(debug=True)