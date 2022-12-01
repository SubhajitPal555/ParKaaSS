import cv2
import numpy as np
import imutils
import argparse
import sys
import time
import pyrebase
import thread
import tensorflow
import mrcnn.model


start_time = time.time()

config = {

    "apiKey": "###",
    "authDomain": "###",
    "databaseURL": "###",
    "projectId": "##",
    "storageBucket": "##",
    "messagingSenderId": "##"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
db.child("Incoming").child("Medium")
db.child("Incoming").child("Large")
db.child("Outgoing").child("Medium")
db.child("Outgoing").child("Large")

fgbg = cv2.creatweBackgroundSubtractorMOG2()

def firebase(bus_count_left, bus_count_right, car_count_left, car_count_right):

    if bus_count_right > 0:
        data = {"Count": str(bus_count_right)}
        db.child("Incoming").child("Large").set(data)
    if car_count_right > 0:
        data = {"Count": str(car_count_right)}
        db.child("Incoming").child("Medium").set(data)
    if bus_count_left > 0:
        data = {"Count": str()}

