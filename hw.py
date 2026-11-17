import cv2
import numpy as np

image = cv2.imread("jetlearn.jpg")

if image is None:
  print("image has not been found")
  exit()

colorchoice = int(input("Enter 1 to open the image, 2 to save it 3 to convert to grayscale 4 to convert to hsv "))

if colorchoice == 1:
  cv2.imshow("original image",image)

elif colorchoice == 2:
  cv2.imwrite("savedimage.jpg",image)

elif colorchoice == 3:
  new = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
  cv2.imshow("grayscale",new)

elif colorchoice == 4:
  new = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
  cv2.imshow("hsv",new)

cv2.waitKey(0)
cv2.destroyAllWindows()
