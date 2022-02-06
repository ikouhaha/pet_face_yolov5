from genericpath import exists
from Util import *
from yattag import Doc, indent
import shutil


img_size = 224

source_path = "D:\IVE\source\cat"
shutil.rmtree("C:/Users/ikouh/Documents/catface")
Path("C:/Users/ikouh/Documents/catface/outputs").mkdir(parents=True, exist_ok=True)


#source_path = "D:/IVE/source/cat"

def saveXML(f,xmin,ymin,xmax,ymax,width,height,depth):
  doc, tag, text = Doc().tagtext()
  img_filename, ext = os.path.splitext(f)
  with tag('doc'):
      with tag('path'):text("C:/Users/ikouh/Documents/catface/cat_{0}".format(f))
      with tag('outputs'):
        with tag('object'):
          with tag('item'):
            with tag('name'):text('cat')
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

  with open('C:/Users/ikouh/Documents/catface/outputs/cat_{0}.xml'.format(img_filename), 'w', encoding='utf-8') as f:
    f.write(result)
    


            
#saveXML("00000018_029.jpg",134,32,260,158,500,400)




for dirs in os.listdir(source_path):
  
  print(dirs)
  dirname = dirs
  base_path = source_path+"/"+dirname
  file_list = sorted(os.listdir(base_path))
  random.shuffle(file_list)

  for f in file_list:
    if '.cat' not in f:
      continue

   

     # if '00000001_000.jpg' not in f:
    #   continue

    # read landmarks
    pd_frame = pd.read_csv(os.path.join(base_path, f), sep=' ', header=None)
    landmarks = (pd_frame.values[0][1:-1]).reshape((-1, 2))

    # load image
    img_filename, ext = os.path.splitext(f)

    img = cv2.imread(os.path.join(base_path, img_filename))

    # resize image and relocate landmarks
    img, ratio, top, left = resize_img(img,img_size)
    landmarks = ((landmarks * ratio) + np.array([left, top])).astype(np.int)
    bb = np.array([np.min(landmarks, axis=0), np.max(landmarks, axis=0)])

    # for l in bb:
    #    cv2.circle(img, center=tuple(l), radius=1, color=(255, 255, 255), thickness=2)

    # plt.imshow(img)
    # plt.show()

    #copy file
    print(img_filename)
    #src = os.path.join(base_path, img_filename)
    dst = 'C:/Users/ikouh/Documents/catface/cat_' +img_filename
    xmin,ymin,xmax,ymax = bb[0][0],bb[0][1],bb[1][0],bb[1][1]
    width,height,depth = img.shape
    saveXML(img_filename,xmin,ymin,xmax,ymax,width,height,depth)
    cv2.imwrite(dst, img)
    
    

    #[new_bb[0][1]:new_bb[1][1], new_bb[0][0]:new_bb[1][0]]
    #cv2.circle(img, center=(bb[0][0],bb[0][1]), radius=2, color=(255, 255, 255), thickness=2)
    #cv2.circle(img, center=(bb[1][0],bb[0][1]), radius=2, color=(255, 255, 255), thickness=2)
    #cv2.circle(img, center=(bb[0][0],bb[1][1]), radius=2, color=(255, 255, 255), thickness=2)
    #cv2.circle(img, center=(bb[1][0],bb[1][1]), radius=2, color=(255, 255, 255), thickness=2)
  
    #plt.imshow(img)
    #plt.show()

        


