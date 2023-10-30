<<<<<<< HEAD
from flask import Flask, jsonify
from flask import request
from backend import TwitchConnect, ProfileManager
from flask_cors import CORS  # <-- Add this import
from MouseInputs import *
=======
from flask import Flask 
from flask import request
from backend import TwitchConnect, ProfileManager
>>>>>>> c46874a2dce852b7500489dc6844aca991bfaf18
import threading

app = Flask(__name__)
t1 = threading.Thread(target=TwitchConnect.twitch, daemon=True)

# Pass the required route to the decorator. 
@app.route("/hello") 
def hello(): 
	return "Hello, Welcome to GeeksForGeeks"

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

<<<<<<< HEAD
@app.route('/create-text-file', methods=['POST'])
def create_text_file_endpoint():
    create_text_file()
    return jsonify({"message": "Text file created successfully!"})

@app.route('/load-allowed-commands', methods=['POST'])
def load_allowed_commands_endpoint():
    commands = load_allowed_commands()
    return jsonify({"commands": commands})

@app.route('/add_allowed_command/<command>', methods=['POST'])
def add_allowed_command_endpoint(command):
    add_allowed_command(command)
    return jsonify({"message": f"Command '{command}' added successfully!"})

if __name__ == "__main__":
	app.run(debug=True) 
	app.run(port=3000)
=======
if __name__ == "__main__":
	app.run(debug=True) 
	app.run(port=3000)
>>>>>>> c46874a2dce852b7500489dc6844aca991bfaf18
