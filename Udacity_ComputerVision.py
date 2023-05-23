import cv2 as cv


image = cv.imread('media/Certificate.jpg',1)
print(image.shape[:])
print(image[25:30][105:109][:])
#imgreen = image[:][:][0]
#print(imgreen)
#cv2.imshow('Img',imgreen)
#cv2.imshow('Img',image[1][0:100][0:100])
cap = cv.VideoCapture(0)
while True:
    isTrue, frame = cap.read()
    cv.imshow("Vid", frame)
    if cv.waitKey(5000):
        break

cap.release()
#cv.waitKey(0)
cv.destroyAllWindows()