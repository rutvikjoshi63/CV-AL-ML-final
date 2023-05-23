import cv2
print("Open CV")

img = cv2.imread('media/Certificate.jpg',-1) #-1 original, 0 b&w, 1 Transparent 
#img = cv2.resize(img,(400, 400))
img = cv2.resize(img,(0, 0),fx=0.7, fy=0.5)
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite("media/New_Certificate.png",img)
print(type(img))
print(img)
print("here",img.shape[0])

print(img[0][10:15])



cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows
