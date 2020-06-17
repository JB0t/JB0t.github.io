#General
import os
#Flask
from flask import Flask, request, jsonify, json, send_from_directory, url_for, render_template
from flask_restful import Resource, Api
#WebBrowser
from urllib.request import urlopen


#Setup
app = Flask(__name__, template_folder="./../")

#Load files
@app.route('/<path:file>', methods=['GET'])
def getFile(file):
    try:
        return send_from_directory(app.template_folder, file)
    except FileNotFoundError:
        pass

#Route
@app.route('/', methods=['GET'])
def route():
    return render_template('index.html')

#Start
if __name__=="__main__":
    app.run(host='0.0.0.0', port=5012, debug=True, extra_files=os.getcwd())
