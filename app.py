from crypt import methods
from flask import Flask, render_template, request, url_for, redirect, session
from controller.fotos import photos_index

app = Flask(__name__)
app.secret_key = "testing"

@app.route('/', methods=['GET'])
def index():
    return render_template('user/index.html')


if __name__ == "__main__":
  app.run(debug=True)