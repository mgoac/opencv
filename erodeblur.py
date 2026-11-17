import numpy as np
import cv2
image = cv2.imread("/home/mgoal/Desktop/Coding/VScode/opencv/Lesson2/pikachu.jpg")

newimage = cv2.erode(image,(5,5),iterations=1)
cv2.imshow("new",newimage)
newimage1 = cv2.GaussianBlur(image,(99,99),0)
cv2.imshow("new1",newimage1)
blur = cv2.blur(image,(99,99))
cv2.imshow("new2",blur)
resize = cv2.resize(image,(400,400))
cv2.imshow("resize",resize)

border = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_CONSTANT, value=[0,0,255])
cv2.imshow("border",border)

border1 = cv2.copyMakeBorder(image,100,100,100,100,cv2.BORDER_REPLICATE, value=[0,0,255])
cv2.imshow("border1",border1)

border2 = cv2.copyMakeBorder(image,100,100,100,100,cv2.BORDER_REFLECT, value=[0,0,255])
cv2.imshow("border2",border2)

border3 = cv2.copyMakeBorder(image,100,100,100,100,cv2.BORDER_WRAP, value=[0,0,255])
cv2.imshow("border3",border3)





cv2.waitKey(0)
cv2.destroyAllWindows()