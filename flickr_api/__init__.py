import flickrapi
from credentials import FLICKR_KEY, FLICKR_SECRET
import json

class Flickr:
    def __init__(self) -> None:
        self.flickr = flickrapi.FlickrAPI(FLICKR_KEY, FLICKR_SECRET, format='json')

    def test(self):
        # photos = self.flickr.photos.search(user_id='73509078@N00', per_page='10')
        # [print(i.getInfo()) for i in photos]
        # return photos

        raw = self.flickr.photosets.getList(user_id='73509078@N00')
        # print( json.loads(raw.decode('utf-8')))
        return json.loads(raw.decode('utf-8'))
        