import cv2,numpy

v=cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True :
    a=0

    area_of_face=0
    area_of_eye = 0
    area_of_face_minus_eye = 0
    face=cv2.CascadeClassifier("C:\Python\haarcascade_frontalface_alt.xml")
    eyes = cv2.CascadeClassifier("C:\Python\haarcascade_eye.xml")

    check,frame=v.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    f=face.detectMultiScale(gray,1.3,5)
    for x,y,w,h in f:
        area_of_face =w*h
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        roi_gray=gray[y:y+h,x:x+w]
        roi_color = frame[y:y + h, x:x + w]
        eye=eyes.detectMultiScale(roi_gray)
        a=len(eye)


        for ex,ey,ew,eh in eye:
            area_of_eye = ew*eh
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
    area_of_face_minus_eyes =area_of_face-area_of_eye

    if area_of_face==area_of_face_minus_eye or a==0:
        print('drowsy')
    else:
        print('ok')

    cv2.imshow("Drowsiness Detection",frame)
    c=cv2.waitKey(1)
    if c==ord('q'):
        break
v.release()
cv2.destroyAllWindows()



