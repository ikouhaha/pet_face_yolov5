
from package import *

if(platform.node()=="LAPTOP-MEFC1PDG"):
    xmlfilepath = "./data/Annotations"
    txtsavepath = "./data/ImageSets"
    labelPath = "./data/labels"
    imgPath = "./data/images"
    # dataset_path = "./dataset"
    # model_path = "./models"
    # result_path = "./result"
    # sample_path = "./samples"
    # logs_path = "./logs" 
    # lmk_logs_path = "./lmk_logs"
    # images_path = "./images" 
else:
    xmlfilepath = "./source/cats"
    txtsavepath = "./data/ImageSets"
    labelPath = "./data/labels"
    imgPath = "./data/images"
    # dataset_path = "./dataset"
    # model_path = "/content/drive/MyDrive/PET_FACE/models"
    # result_path = "/content/drive/MyDrive/PET_FACE/result"
    # sample_path = "/content/drive/MyDrive/PET_FACE/samples"
    # logs_path = "/content/drive/MyDrive/PET_FACE/logs"
    # lmk_logs_path = "/content/drive/MyDrive/PET_FACE/lmk_logs" 
    # images_path = "/content/drive/MyDrive/PET_FACE/images" 

# shutil.rmtree(logs_path,ignore_errors=True)
# shutil.rmtree(lmk_logs_path,ignore_errors=True)

# Path(xmlfilepath).mkdir(parents=True, exist_ok=True)
# Path(txtsavepath).mkdir(parents=True, exist_ok=True)
# Path(labelPath).mkdir(parents=True, exist_ok=True)