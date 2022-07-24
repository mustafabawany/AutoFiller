import cv2 
import os
import numpy as np
import pytesseract
try:
 from PIL import Image
except ImportError:
 import Image

class PreProcessing:
    def __init__(self):
        self.IMG_PATH = "backend/Resume/"

    def ZoomImage(self,img, zoom_factor=2):
        return cv2.resize(img, None, fx= zoom_factor, fy= zoom_factor, interpolation= cv2.INTER_LINEAR)

    def GrayScaleImage(self,img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = 255*(gray < 128).astype(np.uint8) 
        return gray

    def InvertImage(self,img):
        return cv2.bitwise_not(img)

    def CropImage(self,img):
        # Find all non-zero points (text)
        coords = cv2.findNonZero(img) 
        # Find minimum spanning bounding box
        x, y, w, h = cv2.boundingRect(coords) 
        # Crop the image - note we do this on the original image
        img = img[y:y+h, x:x+w] 
        return img 

    def CreateBoundingBox(self,img):
        h, w, c = img.shape
        boxes = pytesseract.image_to_boxes(img) 
        for b in boxes.splitlines():
            b = b.split(' ')
            img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
        return img

    def SaveImage(self , img , image_name):
        cv2.imwrite(self.IMG_PATH + "/" + image_name +'.png', img)

    def ReadImage(self , image_name):
        img = cv2.imread(self.IMG_PATH + "/" + image_name + '.png')
        return img