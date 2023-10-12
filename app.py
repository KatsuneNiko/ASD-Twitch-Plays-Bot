from flask import Flask 
from flask import request
from backend import TwitchConnect, ProfileManager
import threading
import json  

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

@app.route("/StyleOfPlay", methods=['GET', 'POST']) 
def apiSetStyleOfPlay():
	data = request.get_json()
	testSOP = data['SOP']
	if testSOP == 'anarchy':
		TwitchConnect.setStyleOfPlay('anarchy', 5)
	else:
		TwitchConnect.setStyleOfPlay('democratic', 5)
	return json.dumps({"result":"success"}) 
	
@app.route("/") 
def index():
	return "Homepage of GeeksForGeeks"

if __name__ == "__main__":
	app.run(debug=True) 
	app.run(port=3000)
