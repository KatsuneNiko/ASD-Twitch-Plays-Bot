from flask import Flask, jsonify
from MouseInputs import *

app = Flask(__name__)

@app.route('/create-text-file', methods=['POST'])
def create_text_file_endpoint():
    create_text_file()
    return jsonify({"message": "Text file created successfully!"})

if __name__ == '__main__':
    app.run(port=5000)
