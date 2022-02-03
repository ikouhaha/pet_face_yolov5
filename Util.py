
from package import *

googlePath = "/content/drive/MyDrive/pet_face_yolo/data"
xmlfilepath = "data/Annotations"
txtsavepath = "data/ImageSets"
labelPath = "data/labels"
imgPath = "data/images"
dataPath = "data"


def createPath():
    Path(xmlfilepath).mkdir(parents=True, exist_ok=True)
    Path(txtsavepath).mkdir(parents=True, exist_ok=True)
    Path(labelPath).mkdir(parents=True, exist_ok=True)
    Path(imgPath).mkdir(parents=True, exist_ok=True)
    Path(dataPath).mkdir(parents=True, exist_ok=True)