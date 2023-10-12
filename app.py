from flask import Flask 
from flask import request
from backend import TwitchConnect
from backend import ConsoleMenu
import json  


app = Flask(__name__) 

# Pass the required route to the decorator. 
@app.route("/hello") 
def hello(): 
    return "Hello, Welcome to GeeksForGeeks"

@app.route("/StyleOfPlay") 
def StyleOfPlay(): 
	return {
		"getSOP": TwitchConnect.styleOfPlay,
		"SOP": "anarchy",
		"triggerSOP": TwitchConnect.setStyleOfPlay()
    }

@app.route("/StyleOfPlay", methods=['GET', 'POST']) 
def apiSetStyleOfPlay():
	data = request.get_json()
	testSOP = data['SOP']
	if testSOP == 'anarchy':
		TwitchConnect.setStyleOfPlay('anarchy', 5)
	else:
		TwitchConnect.setStyleOfPlay('democratic', 5)
	return json.dumps({"result":"success"}) 
        
@app.route("/CRUDKeyboard") 
def StyleOfPlay(): 
	return {
		"getSOP": TwitchConnect.styleOfPlay,
		"SOP": "anarchy",
		"triggerSOP": TwitchConnect.setStyleOfPlay()
    }
	
@app.route("/") 
def index(): 
	return "Homepage of GeeksForGeeks"

if __name__ == "__main__": 
	app.run(debug=True) 
	app.run(port=5000)
