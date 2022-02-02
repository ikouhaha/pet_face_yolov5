
from package import *

googlePath = "/content/drive/MyDrive/pet_face_yolo/data"


xmlfilepath = "data/Annotations"
txtsavepath = "data/ImageSets"
labelPath = "data/labels"
imgPath = "data/images"



def syncFile():
    Path(xmlfilepath).mkdir(parents=True, exist_ok=True)
    Path(txtsavepath).mkdir(parents=True, exist_ok=True)
    Path(labelPath).mkdir(parents=True, exist_ok=True)
    Path(imgPath).mkdir(parents=True, exist_ok=True)

    if(os.path.exists(googlePath)):
        shutil.rmtree(xmlfilepath,ignore_errors=True)
        shutil.rmtree(imgPath,ignore_errors=True)
        shutil.copy(googlePath+"/Annotations", xmlfilepath)
        shutil.copy(googlePath+"/images", imgPath)
