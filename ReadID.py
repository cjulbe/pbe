#!/usr/bin/env python
from time import sleep
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
GPIO.cleanup()

try:
    while True:
        print("Hold a tag near the reader")
        id,text = reader.read()
        print("ID: %s\n" % (hex(id)))
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise



