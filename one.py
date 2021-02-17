import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")

img = cv2.imread("faces/pc7r5zrKi.jpeg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.04, minNeighbors=5)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w, y+h), (0,255,0),3)

cv2.imshow("cat face", img)
cv2.waitKey()