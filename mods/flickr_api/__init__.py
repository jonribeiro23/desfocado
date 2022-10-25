import flickrapi
from credentials import FLICKR_KEY, FLICKR_SECRET, USER_ID
import json
import webbrowser
from os import walk
from progress.spinner import MoonSpinner

class FlickerUpload:
    def __init__(self, folder) -> None:
        self.flickr = flickrapi.FlickrAPI(FLICKR_KEY, FLICKR_SECRET)
        self.user_id = USER_ID
        self.folder = folder

        self._verify_permissions()

    def upload(self):
        with MoonSpinner('Processing…') as bar:
            for (dirpath, dirnames, filenames) in walk(self.folder):
                for photo in filenames:
                    self.flickr.upload(f"{dirpath}/{photo}")
                    bar.next()
                    

    def _verify_permissions(self):
        if not self.flickr.token_valid(perms='write'):

            self.flickr.get_request_token(oauth_callback='oob')

            authorize_url = self.flickr.auth_url(perms='write')
            webbrowser.open_new_tab(authorize_url)

            verifier = str(input('Verifier code: '))
            self.flickr.get_access_token(verifier)


class Flickr:
    def __init__(self) -> None:
        self.flickr = flickrapi.FlickrAPI(FLICKR_KEY, FLICKR_SECRET, format='json')
        self.user_id = USER_ID

        self._verify_permissions()

    def photo_info(self):
        photos = self.flickr.photos.search(user_id=self.user_id, extras='url_c')
        res = json.loads(photos.decode('utf-8'))
        return res['photos']['photo']

    def get_photos_url(self):
        photos = self.photo_info()
        for photo in photos:
            yield {
                'url': photo['url_c']
            }

    def delete_all(self):
        photos = self.photo_info()
        for photo in photos:
            self.delete(photo['id'])

    def delete(self, photo_id):
        return self.flickr.photos.delete(photo_id=photo_id)

    def _verify_permissions(self):
        if not self.flickr.token_valid(perms='write'):

            self.flickr.get_request_token(oauth_callback='oob')

            authorize_url = self.flickr.auth_url(perms='write')
            webbrowser.open_new_tab(authorize_url)

            verifier = str(input('Verifier code: '))
            self.flickr.get_access_token(verifier)

        if not self.flickr.token_valid(perms='delete'):

            self.flickr.get_request_token(oauth_callback='oob')

            authorize_url = self.flickr.auth_url(perms='delete')
            webbrowser.open_new_tab(authorize_url)

            verifier = str(input('Verifier code: '))

            self.flickr.get_access_token(verifier)

