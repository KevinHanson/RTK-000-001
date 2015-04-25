##Simple motor script for the RTK-000-001
import RPi.GPIO as GPIO
import time
print 'Set to broadcom pin numbers'
GPIO.setmode(GPIO.BCM)

print 'Motor 1 = Pins 17 and 18'
print 'Motor 2 = Pins 22 and 23'
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

print 'Now loop forever turning one direction for 5 seconds, then the other'
while (True):
	print 'Sleep 1 second then turn 17 on'
	GPIO.output(18, 0)
	time.sleep(1)
	GPIO.output(17, 1);
	time.sleep(5);
	print 'And now the other way round'
	GPIO.output(17, 0)
	time.sleep(1);
	GPIO.output(18, 1);
	time.sleep(5);
	print 'And loop back around'
print 'And final cleanup'
GPIO.cleanup()
