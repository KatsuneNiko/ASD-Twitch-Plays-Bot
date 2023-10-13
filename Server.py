from flask import Flask, jsonify
from flask_cors import CORS  # <-- Add this import
from MouseInputs import *

app = Flask(__name__)
CORS(app)  # <-- Add this line to enable CORS for the entire app

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


if __name__ == '__main__':
    app.run(port=5000)
