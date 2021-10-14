from flask import Flask
from flask import request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <div style="width: 90vw; height: 90vh; display: flex; align-items:center; justify-content: center;">
      <form action="/parser" method="POST">
        Enter a URL  : <input type="text" name="url"><br>
        Enter a HTML Tag : <input type="text" name="tag"><br>
        <input type="submit" value="Submit">
      </form>
    </div>
    """

@app.route('/parser', methods=['POST'])
def parser():
    url = request.form.get('url')
    tag = request.form.get('tag')
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    interested = soup.find_all(tag)
    return str(interested)

if __name__ == '__main__':
  app.run()