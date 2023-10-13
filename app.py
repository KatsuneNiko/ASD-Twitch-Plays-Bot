from flask import Flask 
from flask import jsonify 
from flask import request
from flask_cors import CORS
from backend import TwitchConnect
from backend import ConsoleMenu
import json  


app = Flask(__name__) 

# Pass the required route to the decorator. 
@app.route("/hello") 
def hello(): 
    return "Hello, Welcome to GeeksForGeeks"

@app.route("/StyleOfPlay", methods=['GET']) 
def StyleOfPlay():
	currentSOP = TwitchConnect.styleOfPlay
	if request.method == 'POST':
		print('post app')
	if currentSOP == 'anarchy':
		TwitchConnect.setStyleOfPlay('democratic', 5)
	else:
		TwitchConnect.setStyleOfPlay('anarchy', 5) 
	return {
		"getSOP": TwitchConnect.styleOfPlay,
		"SOP": "anarchy"
    }

@app.route('/StyleOfPlay', methods=['POST'])
def postStyleOfPlay():
	currentSOP = TwitchConnect.styleOfPlay
	if request.method == 'POST':
		print('post app')
	if currentSOP == 'anarchy':
		TwitchConnect.setStyleOfPlay('democratic', 5)
	else:
		TwitchConnect.setStyleOfPlay('anarchy', 5)
	return {
		"getSOP": TwitchConnect.styleOfPlay,
		"SOP": "anarchy"}
	
        
@app.route("/CRUDKeyboard") 
def test(): 
	return {
		"getSOP": TwitchConnect.styleOfPlay,
		"SOP": "anarchy",
    }
	
@app.route("/ignore") 
def index(): 
	return "Homepage of GeeksForGeeks"

if __name__ == "__main__": 
	app.run(debug=True) 
	app.run(port=5000)
