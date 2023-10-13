from flask import Flask 
from flask import jsonify 
from flask import request
<<<<<<< HEAD
from backend import TwitchConnect, ProfileManager
import threading
=======
from flask_cors import CORS
from backend import TwitchConnect
from backend import ConsoleMenu
>>>>>>> 22d43e4a33ca008fc055f078e72661763954ad6a
import json  

app = Flask(__name__)
t1 = threading.Thread(target=TwitchConnect.twitch, daemon=True)

# Pass the required route to the decorator. 
@app.route("/hello") 
def hello(): 
	return "Hello, Welcome to GeeksForGeeks"

<<<<<<< HEAD
@app.route("/TwitchConnect", methods=['GET', 'POST'])
def apiTwitchConnect():
	if request.method == 'POST':
		body = request.get_json()
		if body['active']:
			t1.start()
		else:
			TwitchConnect.pauseEvent.set()
	return {
		"active": t1.is_alive()
	}

@app.route("/ProfileManager", methods=['GET', 'POST'])
def apiProfile():
	if request.method == 'POST':
		body = request.get_json()
		if body['method'] == 'create':
			ProfileManager.createProfile(body['name'])
		elif body['method'] == 'delete':
			ProfileManager.deleteProfile(body['name'])
		elif body['method'] == 'select':
			print(ProfileManager.profileExists(ProfileManager.profile))
			ProfileManager.profile = body['name']
	return {
		"currentProfile": ProfileManager.profile,
		"profileNames": ProfileManager.listProfiles(),
	}
=======
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
>>>>>>> 22d43e4a33ca008fc055f078e72661763954ad6a

@app.route('/StyleOfPlay', methods=['POST'])
def postStyleOfPlay():
	currentSOP = TwitchConnect.styleOfPlay
	if request.method == 'POST':
		print('post app')
	if currentSOP == 'anarchy':
		TwitchConnect.setStyleOfPlay('democratic', 5)
<<<<<<< HEAD
	return json.dumps({"result":"success"}) 
	
@app.route("/") 
def index():
=======
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
>>>>>>> 22d43e4a33ca008fc055f078e72661763954ad6a
	return "Homepage of GeeksForGeeks"

if __name__ == "__main__":
	app.run(debug=True) 
	app.run(port=3000)
