from Util import *
import zipfile

base_path = "C:/Users/ikouh/Documents/catface/"

base_path2 = "C:/Users/ikouh/Documents/dogface/"
zf = zipfile.ZipFile('{}.zip'.format("G:/My Drive/pet_face_yolo/data/data"), 'w', zipfile.ZIP_DEFLATED)

result =""
for f in os.listdir(base_path):
    if f == "outputs":
        continue
    #result = result+"\n" +f
    print(f)
    img_filename, ext = os.path.splitext(f)
    src = os.path.join(base_path, f)
    src2 = os.path.join(base_path,"outputs/{0}.xml".format(img_filename))
    
    zf.write(src,"images/"+f)
    zf.write(src2,"Annotations/"+img_filename+".xml")
    #os.remove(dst)
    #os.remove(dst2)
    #shutil.copy(src,dst)
    #shutil.copy(src2,dst2)

# with open('temp.txt', 'w', encoding='utf-8') as f:
#     f.write(result)

for f in os.listdir(base_path2):
    if f == "outputs":
        continue
    #result = result+"\n" +f
    print(f)
    img_filename, ext = os.path.splitext(f)
    src = os.path.join(base_path2, f)
    src2 = os.path.join(base_path2,"outputs/{0}.xml".format(img_filename))
    
    zf.write(src,"images/"+f)
    zf.write(src2,"Annotations/"+img_filename+".xml")
    #os.remove(dst)
    #os.remove(dst2)
    #shutil.copy(src,dst)
    #shutil.copy(src2,dst2)

# with open('temp.txt', 'w', encoding='utf-8') as f:
#     f.write(result)

print(result)

# src = os.path.join(base_path, img_filename)
# dst = os.path.join('C:/Users/ikouh/Documents/catface/', img_filename)
# xmin,ymin,xmax,ymax = bb[0][0],bb[0][1],bb[1][0],bb[1][1]
# width,height,depth = img.shape
# saveXML(img_filename,xmin,ymin,xmax,ymax,width,height,depth)
# shutil.copy(src,dst)