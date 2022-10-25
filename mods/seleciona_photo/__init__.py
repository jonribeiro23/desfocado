from os import walk
import cv2
import shutil
from progress.bar import Bar

class SelecionaPhotos:
    def __init__(self, folder) -> None:
        self.photos = []
        self.folder = folder
        self.get_photos()
    
    def variance_of_laplacian(self, image):
        # compute the Laplacian of the image and then return the focus
        # measure, which is simply the variance of the Laplacian
        return cv2.Laplacian(image, cv2.CV_64F).var()

    def get_photos(self):
        for (dirpath, dirnames, filenames) in walk(self.folder):
            self.photos = filenames

    def copy_photo_to_upload(self, source_path):
        destination = './upload'
        shutil.copy(source_path, destination)

    def selecionar(self):
        with Bar('Processing...') as bar:
            for photo in self.photos:
                image = cv2.imread(f"{self.folder}/{photo}", cv2.IMREAD_UNCHANGED)

                scale_percent = 22 # percentual da imagem original
                width = int(image.shape[1] * scale_percent / 100)
                height = int(image.shape[0] * scale_percent / 100)
                dim = (width, height)
                image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                fm = self.variance_of_laplacian(gray)

                if fm >= 60:
                    self.copy_photo_to_upload(f"{self.folder}/{photo}")
                bar.next()
            
