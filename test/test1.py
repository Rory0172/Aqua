import RPi.GPIO as GPIO
import time
from configparser import ConfigParser	


config = ConfigParser()
config.read('./settings.ini')

mlpersec = config.getfloat('mlpersec', 'mlpersec')

pomp_1_gpio = config.getint('gpio', 'pomp_1_gpio')

pomp1insec = 5 * mlpersec

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pomp_1_gpio,GPIO.OUT)
print "Pomp 1 aan voor %d sec om 5 ml te pompen." % (pomp1insec)
GPIO.output(pomp_1_gpio,GPIO.LOW)
time.sleep (pomp1insec)
print 'Pomp 1 uit.'
GPIO.output(pomp_1_gpio,GPIO.HIGH)