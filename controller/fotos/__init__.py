from mods.flickr_api import Flickr

flickr = Flickr()

def photos_index():
    return flickr.get_photos_url()