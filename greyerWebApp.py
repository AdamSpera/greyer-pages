# ---- Workspace setup instructions: ----
# python3 -m venv greyer-env
# greyer-env\scripts\activate
# pip install re
# pip install sys
# pip install json
# pip install lxml
# pip install requests
# pip install beautifulsoup4
# pip install flask

# ---- Running the program ----
# greyer-env\scripts\activate
# flask --app greyerWebApp run 

# ---- Running the program on vm ----
# export FLASK_APP=greyerWebApp.py
# flask run --host=0.0.0.0

from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests, re, sys, json

app = Flask(__name__, template_folder='template', static_folder='static')

@app.route("/")
def sendStatic():
  return render_template('index.html')

@app.route("/getData", methods=['POST'])
def getData():
  postData = json.loads(request.data.decode("utf-8"))
  
  url = 'https://searchpeoplefree.com/find/' + postData["name"].replace(' ', '-') + '/' + postData["state"]

  response = requests.get(url)
  html = response.text

  soup = BeautifulSoup(response.content, 'lxml')

  results = {
      'name': soup.find_all('h2')[0].text.replace("\n", "").split(' in')[0],
      'age': re.sub(' +', ' ', soup.find_all('h3')[0].text.replace("\n", " ")).strip(),
      'address': soup.find_all('address')[0].text.replace("\n", ""),
      'phone': 'No Phone' if soup.find_all('h4')[0].text.replace("\n", "").strip() == 'Email Address' else soup.find_all('h4')[0].text.replace("\n", "").strip().split('-Current')[0],
  }

  return results