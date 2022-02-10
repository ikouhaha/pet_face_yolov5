"""Perform test request"""
import pprint

import requests
from Util import *
import cv2

from utils.plots import Annotator, colors, save_one_box

DETECTION_URL = "http://localhost:5000/pet_face_detect"
TEST_IMAGE = "data\images\WhatsApp Image 2021-10-24 at 15.39.47.jpeg"

image_data = open(TEST_IMAGE, "rb").read()

response = requests.post(DETECTION_URL, files={"image": image_data}).json()

img = cv2.imread(TEST_IMAGE)


if(response["success"] == False):
    exit

#each pred
for res in response["data"] :
    print(res)
    annotator = Annotator(img, line_width=3, example=str("cat"))
    annotator.box_label([res["xmin"],res["ymin"],res["xmax"],res["ymax"]], res["name"] + " {:.2f}".format(res["confidence"]), color=colors(res["class"], True))
    # Stream results
    im0 = annotator.result()
    cv2.imwrite("asdasd.jpg", im0)


#pprint.pprint(response)
