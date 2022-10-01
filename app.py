
from os import walk
import cv2
from progress.bar import Bar

def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

f = []
for (dirpath, dirnames, filenames) in walk('./img'):
    f = filenames

bar = Bar('Processing', max=20)


for photo in f:
    image = cv2.imread('./img/'+photo, cv2.IMREAD_UNCHANGED)

    # minha câmera possui uma resolução muita alta, então precisei redimensionar as fotos
    scale_percent = 22 # percentual da imagem original
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    text = "Not Blurry"
    
    if fm < 60:
        text = "Blurry"
    
    cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow("Image", image)
    key = cv2.waitKey(0)
    bar.next()
bar.finish()