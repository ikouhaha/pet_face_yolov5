
import errno
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

def resize_img(im,img_size):
  old_size = im.shape[:2] # old_size is in (height, width) format
  ratio = float(img_size) / max(old_size)
  new_size = tuple([int(x*ratio) for x in old_size])
  # new_size should be in (width, height) format
  im = cv2.resize(im, (new_size[1], new_size[0]))
  delta_w = img_size - new_size[1]
  delta_h = img_size - new_size[0]
  top, bottom = delta_h // 2, delta_h - (delta_h // 2)
  left, right = delta_w // 2, delta_w - (delta_w // 2)
  new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,
      value=[0, 0, 0])
  return new_im, ratio, top, left   

def copyanything(src, dst):
    try:
        if(not os.path.exists(dst)):
            os.makedirs(dst, exist_ok=True)
            
        copy_tree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno in (errno.ENOTDIR, errno.EINVAL):
            shutil.copy(src, dst)
        else: raise

def emptyFolder(path):
    files = glob.glob(path+'/**/*', recursive=True)      
    for file in files:
        if(os.path.isdir(file)):
            continue
        print(file)
        os.remove(file)
