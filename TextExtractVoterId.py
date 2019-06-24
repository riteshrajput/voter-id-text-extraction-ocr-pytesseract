# -*- coding: utf-8 -*-
"""
@author: Ritesh Rajput | riteshrajput381@gmail.com
This script is used to extract text from the voter ID and stored in testfile.txt
"""

# Libraries
import cv2
import numpy as np
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((7, 6), np.uint8)
    #print(kernel)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite("RemovedNoise.jpg", img)

    # Write the image after apply opencv to do some
    cv2.imwrite('SampleProcess.jpg', img)
    
    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open('SampleProcess.jpg'))

    # Writing Result into text file 
    file = open("TextExtract.txt","w") 
    file.write(result)
    file.close()

    return result

get_string('Sample.jpg')
print ("------ Done -------")