import cv2 as cv
print("Open CV")

img = cv.imread('media/Certificate.jpg') #-1 original, 0 b&w, 1 Transparent 
#img = cv.resize(img,(400, 400))
# img = cv.resize(img,(0, 0),fx=0.7, fy=0.5)
# img = cv.rotate(img,cv.ROTATE_90_CLOCKWISE)
# cv.imwrite("media/New_Certificate.png",img)
# print(type(img))
# print(img)
# print("here",img.shape[0])
# print(img[0][10:15])
cv.imshow("Image", img)
cv.waitKey(0)

capture = cv.VideoCapture('media/1.1.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()

cv.destroyAllWindows
