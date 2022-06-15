"""Perform test request"""
import pprint

import requests
from matplotlib import pyplot as plt
import cv2

from utils.plots import Annotator 

DETECTION_URL = "http://localhost:5000/v1/object-detection/yolov5s"
TEST_IMAGE = "data\images\WhatsApp Image 2021-10-24 at 15.39.47.jpeg"

image_data = open(TEST_IMAGE, "rb").read()

response = requests.post(DETECTION_URL, files={"image": image_data}).json()

img = cv2.imread(TEST_IMAGE)

#each pred
for i in response:
    print(i)
    annotator = Annotator(img, line_width=3, example=str(names))
    plt.imshow(img)
    plt.show()


#pprint.pprint(response)
