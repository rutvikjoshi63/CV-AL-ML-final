import cv2
print("Open CV")

img = cv2.imread('media/Certificate.jpg',-1)


cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows