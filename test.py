from flickr_api import Flickr
from pprint import pprint

t = Flickr()
pho = t.test()
pprint(pho['photosets']['photoset'])
# for i in pho['photosets']['total']:
#     print(i)