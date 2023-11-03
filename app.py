import os
from flask import Flask, send_from_directory
from flask import request
from flask import redirect
from backend import TwitchConnect, ProfileManager, KeyboardInputs
import threading

app = Flask(__name__, static_folder=None)
t1: threading.Thread | None = None

# Pass the required route to the decorator. 
@app.route("/hello") 
def hello(): 
	return "Hello, Welcome to GeeksForGeeks"

@app.route("/TwitchConnect", methods=['GET', 'POST'])
def apiTwitchConnect():
	global t1
	if request.method == 'POST':
		body = request.get_json()
		if body['active']:
			if t1 is None:
				t1 = threading.Thread(target=TwitchConnect.twitch, args=[body.get('channelName') if body.get('channelName') is not None else ''])
			TwitchConnect.exitEvent.clear()
			t1.start()
		else:
			TwitchConnect.exitEvent.set()
			t1.join()
			t1 = None
	return {
		"active": t1 is not None and t1.is_alive()
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
	body = request.get_json()
	if body['trigger'] == 'true':
		if currentSOP == 'anarchy':
			TwitchConnect.setStyleOfPlay('democratic', 5)
		else:
			TwitchConnect.setStyleOfPlay('anarchy', None)
	return {
		"getSOP": TwitchConnect.styleOfPlay,
		}
        
@app.route("/CRUDKeyboard", methods=['GET']) 
def CRUDKeyboard(): 
	return {
		"txtArray": ProfileManager.viewProfileAPI(),
		"profileName": ProfileManager.returnProfile(),
    }

@app.route('/CRUDKeyboard', methods=['POST']) 
def postCRUDKeyboard(): 
	body = request.form
	print(body)
	if(body['formOneOrTwo'] == 'add'):
		action = body['action']
		duration = body['duration']
		keyword = body['keyword']
		keybind = body['keybind']
		currentProfile = ProfileManager.returnProfile()
		KeyboardInputs.apiAddKeybind(action, duration, keyword, keybind, currentProfile)
	elif (body['formOneOrTwo'] == 'delete'):
		keyword = body['deleteKeyword']
		currentProfile = ProfileManager.returnProfile()
		KeyboardInputs.apiDeleteKeybind(keyword, currentProfile)
		print("At API, when delete, profile = ", ProfileManager.profile)
	return redirect("http://localhost:3000/CRUDKeyboard", code=302)

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def catch_all(path):
	try:
		return send_from_directory('build', path)
	except:
	    return send_from_directory('build', 'index.html')

@app.route("/ignore") 
def index(): 
	return "Homepage of GeeksForGeeks"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=3000, debug=(os.getenv('ENV') != 'production'))