from Util import *
from yattag import Doc, indent
import xml.etree.ElementTree as ET
import shutil

# facePath = "C:/Users/ikouh/Documents/dogface"
xmlPathSource = "D:\IVE\source\dog/annotations/xmls"
facePathSource = "D:\IVE\source\dog/images"
img_size = 224

shutil.rmtree("C:/Users/ikouh/Documents/dogface")
Path("C:/Users/ikouh/Documents/dogface/outputs").mkdir(parents=True, exist_ok=True)

def readXmlBBS(xmlPath):
    
    tree = ET.parse(xmlPath)
    root = tree.getroot()
    xmin = int(root.findall('.//xmin')[0].text)
    ymin = int(root.findall('.//ymin')[0].text)
    xmax = int(root.findall('.//xmax')[0].text)
    ymax = int(root.findall('.//ymax')[0].text)

    return xmin,ymin,xmax,ymax

def saveXML(f,xmin,ymin,xmax,ymax,width,height,depth):
  doc, tag, text = Doc().tagtext()
  img_filename, ext = os.path.splitext(f)
  with tag('doc'):
      with tag('path'):text("C:/Users/ikouh/Documents/dogface/dog_{0}".format(f))
      with tag('outputs'):
        with tag('object'):
          with tag('item'):
            with tag('name'):text('dog')
            with tag('bndbox'):
              with tag('xmin'):text(str(xmin))
              with tag('ymin'):text(str(ymin))
              with tag('xmax'):text(str(xmax))
              with tag('ymax'):text(str(ymax))
      with tag('time_labeled'):text("1643873831694")
      with tag('labeled'):text("true")
      with tag('size'):
        with tag('width'):text(str(width))
        with tag('height'):text(str(height))
        with tag('depth'):text(str(depth))

  result = "<?xml version=\"1.0\" ?> \n" + indent(
  doc.getvalue(),
  indentation = ' '*4,
  newline = '\n'
  )

  with open('C:/Users/ikouh/Documents/dogface/outputs/dog_{0}.xml'.format(img_filename), 'w', encoding='utf-8') as f:
    f.write(result)
        

i = 0
for f in os.listdir(facePathSource):
  if not f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
    continue

  if  f.startswith(('Abyssinian', 'Bengal', 'Bombay'
  ,'British', 'Egyptian', 'Main','Persian','Ragdoll', 'Birman'
  ,'Russian','Siamese','Sphynx' 
  )):
    os.remove(facePathSource+"/"+f)
    continue
  
  print(f)
  img_filename, ext = os.path.splitext(f)
  xmlPath = xmlPathSource+"/{}.xml".format(img_filename)
  isExistsXMLPath = True
  if not (os.path.exists(xmlPath)):
      shutil.move(os.path.join(facePathSource, f),"D:\IVE\source\dog\pending/"+f)
      isExistsXMLPath = False
      continue

  
  
  
  img = cv2.imread(os.path.join(facePathSource, f))
  
  if(img is None):
    continue
  
  
  img, ratio, top, left = resize_img(img,img_size)
  width,height,depth = img.shape
  dst = 'C:/Users/ikouh/Documents/dogface/dog_'+ f
  cv2.imwrite(dst, img)
  if isExistsXMLPath == True:
    xmin,ymin,xmax,ymax = readXmlBBS(xmlPath)
    bb = np.array([(xmin,ymin),(xmax,ymax)])
    bb = ((bb * ratio) + np.array([left, top])).astype(np.int)
  #   bb = np.array([np.min(landmarks, axis=0), np.max(landmarks, axis=0)])
    
    xmin,ymin,xmax,ymax = bb[0][0],bb[0][1],bb[1][0],bb[1][1]
    saveXML(f,xmin,ymin,xmax,ymax,width,height,depth)
  
  
  
  # print (bb)
  # for l in bb:
  #   cv2.circle(img, center=tuple(l), radius=1, color=(255, 255, 255), thickness=2)

  # plt.imshow(img)
  # plt.show()
    
  
  
  i = i+1