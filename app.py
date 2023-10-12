from flask import Flask 
from backend import TwitchConnect
from backend import ConsoleMenu

app = Flask(__name__) 

# Pass the required route to the decorator. 
@app.route("/hello") 
def hello(): 
    return "Hello, Welcome to GeeksForGeeks"

@app.route("/StyleOfPlay") 
def StyleOfPlay(): 
	return {
		"getSOP": TwitchConnect.styleOfPlay
    }
	
@app.route("/") 
def index(): 
	return "Homepage of GeeksForGeeks"

if __name__ == "__main__": 
	app.run(debug=True) 
	app.run(port=5000)
