#!/usr/bin/python

from time import sleep
import os

def timer(time=0):
    for i in range(0,time):
        sleep(1)
        print(i)
    os.system("mpv "+str(os.getcwd())+"/bell.wav")

default = 50
while True:
    time = input("time in seconds (default {} s): ".format(default))
    if not time:
        time = default
    else:
        time = int(time)

    timer(time=time)
    default = time
