import flickrapi
from credentials import FLICKR_KEY, FLICKR_SECRET, USER_ID
import json
import webbrowser


class Flickr:
    def __init__(self) -> None:
        self.flickr = flickrapi.FlickrAPI(FLICKR_KEY, FLICKR_SECRET)
        self.user_id = USER_ID

        self._verify_permissions()

    def photo_info(self):
        photos = self.flickr.photos.search(user_id=self.user_id)
        res = json.loads(photos.decode('utf-8'))
        return res['photos']['photo']

    def _mount_photo_url(self, photo):
        return f"https://live.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}_b.jpg"

    def get_photos_url(self):
        photos = self.photo_info()
        for photo in photos:
            yield {
                'url': self._mount_photo_url(photo)
            }

    def upload(self, photo):
        return self.flickr.upload(photo)

    def _verify_permissions(self):
        if not self.flickr.token_valid(perms='write'):

            # Get a request token
            self.flickr.get_request_token(oauth_callback='oob')

            # Open a browser at the authentication URL. Do this however
            # you want, as long as the user visits that URL.
            authorize_url = self.flickr.auth_url(perms='write')
            webbrowser.open_new_tab(authorize_url)

            # Get the verifier code from the user. Do this however you
            # want, as long as the user gives the application the code.
            verifier = str(input('Verifier code: '))

            # Trade the request token for an access token
            self.flickr.get_access_token(verifier)

    def test(self):
        return self.get_photo_url('52422862629')
