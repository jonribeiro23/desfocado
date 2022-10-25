from flask import render_template
from controller.fotos import photos_index

class Home:
    def index():
        photos = photos_index()
        return render_template('user/index.html', photos=photos)