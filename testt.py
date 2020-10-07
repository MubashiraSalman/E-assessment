import cv2
import math
import itertools
import win32api
from selenium import webdriver


def calculatedistance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


driver = webdriver.Chrome('chromedriver.exe')
cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascPath)
noseCascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')


video_capture = cv2.VideoCapture(0)
driver.get('http://127.0.0.1:999/testpage.html')
currentFrame = 0
count = 0
var = 20

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    noses = noseCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (ex, ey, ew, eh) in noses:
        cv2.circle(frame, (ex + (ew // 2), ey + (eh // 2)), 2, (255, 0, 0), -1)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        for faces, noses in itertools.product([x, y, w, h], [ex, ey, ew, eh]):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # cv2.rectangle(frame, (ex, ey), ((ex+ew), (ey+eh)), (0, 255, 0), 2)
            # d = calculatedistance(x+(w//2), y+(h//2), (x+w), y+(h//2))
            # cv2.circle(frame, (x+(w//2), y+(h//2)), 2, (255, 0, 0), -1)  # center
            # cv2.circle(frame, ((x+w), y+(h//2)), 2, (255, 0, 0), -1)  # right
            cv2.line(frame, (ex + (ew // 2), ey + (eh // 2)), ((x+w), y+(h//2)), (255, 0, 0), 2)  # center to right
            d1 = calculatedistance(ex + (ew // 2), ey + (eh // 2), (x+w), y+(h//2))  # distance center to right
            # cv2.circle(frame, (x, y + (h // 2)), 2, (255, 0, 0), -1)  # left
            cv2.line(frame, (ex + (ew // 2), ey + (eh // 2)), (x, y + (h // 2)), (255, 0, 0), 2)  # center to left
            d2 = calculatedistance(ex + (ew // 2), ey + (eh // 2), x, y + (h // 2))  # distance center to left
            # cv2.circle(frame, ((x + (w // 2)), y), 2, (255, 0, 0), -1)  #top
            cv2.line(frame, (ex + (ew // 2), ey + (eh // 2)), ((x + (w // 2)), y), (255, 0, 0), 2)  # center to top
            # d1 = calculatedistance(ex + (ew // 2), ey + (eh // 2), x + (w // 2), y)  # distance center to top
            # cv2.circle(frame, ((x + (w // 2)), y + h), 2, (255, 0, 0), -1)  #bottom
            cv2.line(frame, (ex + (ew // 2), ey + (eh // 2)), ((x + (w // 2)), y + h), (255, 0, 0), 2)  # center to bottom
            # d2 = calculatedistance(ex + (ew // 2), ey + (eh // 2), x + (w // 2), y + h)  # distance center to bottom
            if currentFrame == var:
                var += 20
                if d1 > 50.0 or d2 > 50.0:
                    win32api.MessageBox(0, 'Warning!', 'Alert')
                    count += 1
                print(currentFrame)
                print("distance center to right")
                print(d1)
                print("distance center to left")
                print(d2)

    # Display the resulting frame
    cv2.imshow('Video', frame)
    currentFrame += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        driver.quit()
        break
    elif count >= 3:
        driver.quit()
        break


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
