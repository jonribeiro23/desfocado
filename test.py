from itertools import count
from numpy import array
from flickr_api import Flickr, FlickerUpload
from pprint import pprint
import os.path
from os import walk
from seleciona_photo import SelecionaPhotos
import pymongo

from credentials import MONGO_URL

def flickr_test():
    t = Flickr()

    up = FlickerUpload('./upload')
    # t.delete_all()

    # Selecionar e fazer upload
    selecionador = SelecionaPhotos('./img')
    selecionador.selecionar()

    print(up.upload())


def db_test():
    # set a 5-second connection timeout
    client = pymongo.MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)

    try:
        print(client.server_info())
    except Exception:
        print("Unable to connect to the server.")



