from crypt import methods
from flask import Flask
from controller.home import Home

app = Flask(__name__)
app.secret_key = "testing"

@app.route('/', methods=['GET'])
def index():
    return Home.index()

@app.route('/login', methods=['GET'])
def login():
    return Home.login()

@app.route('/logar', methods=['GET'])
def logar():
    return Home.logar()


if __name__ == "__main__":
  app.run(debug=True)