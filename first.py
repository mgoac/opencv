import cv2
import numpy as np

image = cv2.imread("jetlearn.jpg")

if image is None:
  print("image has not been found")
  exit()

colorchoice = int(input("Enter 1 for Grayscale, 2 for HSV, 3 for BGR, 4 to save file: "))
save = int(input("Enter 1 to save, and 2 to discard and only show"))
if colorchoice == 1:
  new = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
  cv2.imshow("grayscale",new)

elif colorchoice == 2:
  new = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
  cv2.imshow("hsv",new)

elif colorchoice == 3:
  new = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
  cv2.imshow("bgr",new)

else:
  print("Not a valid choice")


if save == 1:
  cv2.imwrite("savedimage.jpg",new)
elif save == 2:
  pass
else:
  print("Not a valid choice")
  cv2.destroyAllWindows()


blue,green,red = cv2.split(image)
zeros = np.zeros_like(blue)

cv2.imshow("blue",cv2.merge([blue,zeros,zeros]))
cv2.imshow("green",cv2.merge([zeros,green,zeros]))
cv2.imshow("red",cv2.merge([zeros,zeros,red]))

cv2.waitKey(0)
cv2.destroyAllWindows()
