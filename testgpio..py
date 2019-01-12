#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
print "Menu"
GPIO.output(6,GPIO.HIGH)
time.sleep(0.2)
GPIO.output(6,GPIO.LOW)
time.sleep(0.2)
print "Omlaag"
GPIO.output(19,GPIO.HIGH)
time.sleep(0.2)
GPIO.output(19,GPIO.LOW)
time.sleep(0.2)
print "Omlaag"
GPIO.output(19,GPIO.HIGH)
time.sleep(0.2)
GPIO.output(19,GPIO.LOW)
time.sleep(0.2)
print "Omlaag"
GPIO.output(19,GPIO.HIGH)
time.sleep(0.2)
GPIO.output(19,GPIO.LOW)
time.sleep(0.2)
print "Omlaag"
GPIO.output(19,GPIO.HIGH)
time.sleep(0.2)
GPIO.output(19,GPIO.LOW)
time.sleep(0.2)
print "Menu"
GPIO.output(6,GPIO.HIGH)
time.sleep(0.2)
GPIO.output(6,GPIO.LOW)
