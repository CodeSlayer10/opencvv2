import cv2
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import requests


class Api1:
    def __init__(self, first, second=None):
        self.first = first
        self.second = second

    def Show(self):
        link = "http://127.0.0.1:5002/{}".format(self.first)  # link that is going to be used
        resp = requests.get(link)
        if resp.status_code != 200:
            print(resp.status_code)
        else:
            str_content = resp.content.decode()
            #print(str_content)
            return str_content

    def UpdateBool(self):
        link = "http://127.0.0.1:5002/{}/{}".format(self.first, self.second)  # link that is going to be used
        resp = requests.get(link)
        if resp.status_code != 200:
            print(resp.status_code)

        else:
            str_content = resp.content.decode()
            #print(str_conten
            # t)
            return str_content








item12 = Api1("SB")
item = item12.Show()
boolz = item[8]
item13 = Api1("SID")
item1 = item13.Show()
id = item1[8:-3]
item11 = Api1("ID", "is_human_here = 1, id = {}".format(id))
print(item1)
print(id)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
# smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

video_capture = cv2.VideoCapture(0)
while True:
    ret, frame1 = video_capture.read()
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray1, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 0, 250), 2)
        if boolz != 1:
            item11.UpdateBool()


    cv2.imshow('video', frame1)
   # if cv2.waitKey(1) & 0xff == ord('q'):
    #    break
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
video_capture.release()
cv2.destroyAllWindows()










