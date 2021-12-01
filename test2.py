from flask import Flask, json, jsonify, abort, request
import requests

folder = "templates/downloads/sample.txt"
url = "https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt"

app = Flask(__name__)

def dFunction():
   dRequest = request.get(url)

@app.route('/manage_file', methods=['GET', 'POST'])
def manage_file():
    url = 'https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt'
    filename = 'sample.txt'
    if (request.method == 'POST'):
        json_payload = request.get_json()
        if (json_payload['action'] == "download"):
            req = requests.get(url)
            with open(filename, 'download') as file:
                return filename, 201
        
        elif (json_payload['action'] == "read"):
            with open(filename,"read") as file:
                content = file.read()
            return jsonify(content), 200
        
        else:
            abort(400)
        
if __name__ == '__main__':
    app.run(debug=True)