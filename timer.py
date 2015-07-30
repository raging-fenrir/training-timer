#!/usr/bin/python

from time import sleep
import os

def timer(time=50):
    for i in range(0,time):
        sleep(1)
        print(i)
    os.system("mpv "+str(os.getcwd())+"/bell.wav")

while True:
    time = input("time in seconds (default 50 s): ")
    if not time:
        time = 50
    else:
        time = int(time)
    timer(time=time)
