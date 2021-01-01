import cv2
img = cv2.imread("image5.jpeg")
cv2.imshow("testing",img)
cv2.waitKey(0)

##extract image and save
img = img[327:374,145:660,:]
cv2.imshow("testing",img)
cv2.waitKey(0)
cv2.imwrite("email.jpeg",img)