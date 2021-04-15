# imporintg the required libraries.
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

# reading our image
image = cv2.imread('1.PNG')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#######################
# image to string
#######################
#print(pytesseract.image_to_string(image))

#######################
# detecting characters
#######################
'''
after using the image_to_boxes method, we get the co-ordinates for each of the characters.
'''
#print(pytesseract.image_to_boxes(image))
htImage, wdthImg, _ = image.shape
boxes = pytesseract.pytesseract.image_to_boxes(image)
for box in boxes.splitlines():
    print(box)
    box = box.split(' ')
    print(box)
    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv2.rectangle(image, (x, htImage-y), (w, htImage-h), (0, 255, 0), 2)


cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()