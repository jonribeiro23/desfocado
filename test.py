from itertools import count
from numpy import array
from flickr_api import Flickr, FlickerUpload
from pprint import pprint
import os.path
from os import walk
from seleciona_photo import SelecionaPhotos

t = Flickr()
up = FlickerUpload('./upload')

selecionador = SelecionaPhotos('./img')
selecionador.selecionar()

print(up.upload())

