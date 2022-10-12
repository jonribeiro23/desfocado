from itertools import count
from numpy import array
from flickr_api import Flickr
from pprint import pprint
import os.path
from os import walk

t = Flickr()
# pho = t.get_photos_url()
# pprint(pho)
# for i in pho:
#     print(i)

class FilePhoto(object):
    def __init__(self, filename, callback):
        self.file = open(filename, 'rb')
        self.callback = callback
        # the following attributes and methods are required
        self.len = os.path.getsize(filename)
        self.fileno = self.file.fileno
        self.tell = self.file.tell

    def read(self, size):
        if self.callback:
            self.callback(self.tell() * 100 // self.len)
        return self.file.read(size)


def callback(progress):
    print(progress)


class Photo(object):
    def __init__(self, filename, fileobj) -> None:
        self.filename = filename
        self.fileobj = fileobj

params = {'filename': 'img/IMG_3520.JPG'}
params['fileobj'] = FilePhoto(params['filename'], callback)

# photo = t.upload(params)

files = []
for (dirpath, dirnames, filenames) in walk('img'):
    qtd = len(filenames)
    counter = 1
    for photo in filenames:
        try:
            t.upload(str(f"{dirpath}/{photo}"))
            print(100 * (counter / qtd) + photo)
        except Exception:
            pass
        counter += 1

# res = t.upload('img/DSCF8850.jpg')

# print(res.attrib)

# t.upload(photo)