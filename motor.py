##Simple motor script for the RTK-000-001
import RPi.GPIO as GPIO
import time
print 'Set to broadcom pin numbers'
GPIO.setmode(GPIO.BCM)

print 'Motor 1 = Pins 17 and 18'
print 'Motor 2 = Pins 22 and 23'
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)a



def right_forward():
    stop(17)
    start(18)

def right_back():
    stop(18)
    start(17)

def left_forward():
    stop(22)
    start(23)

def left_back():
    stop(23)
    start(22)

def forward(sec):
    print '-----------------FORWARD---------------------'
    right_forward()
    left_forward()
    time.sleep(sec)

def back(sec):
    print '-----------------BACK---------------------'
    right_back()
    left_back()
    time.sleep(sec)
    
def right(sec):
    print '-----------------RIGHT---------------------'
    left_forward()
    right_back()
    time.sleep(sec)

def left(sec):
    print '-----------------LEFT---------------------'
    left_back()
    right_forward()
    time.sleep(sec)

def stop(wheel):
    GPIO.output(wheel, 0)

def start(wheel):
    GPIO.output(wheel, 1)
    
print 'Now loop forever turning one direction for 5 seconds, then the other'
while (True):
    stop(17)
    stop(18)
    stop(22)
    stop(23)           
    time.sleep(5)
    
    forward(.7)
    right(.3)
    forward(.4)
    left(.3)
    forward(1)
    left(.3)
    forward(.5)
    
    
print 'And final cleanup'
GPIO.cleanup()


