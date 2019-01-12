import RPi.GPIO as GPIO
import time
from configparser import ConfigParser

# instantiate
config = ConfigParser()

# parse existing file
config.read('settings.ini')

# read values from a section
doseerpompgpio1 = config.getint('gpio', 'doseerpompgpio1')
#bool_val = config.getboolean('section_a', 'bool_val')
#int_val = config.getint('section_a', 'int_val')
#float_val = config.getfloat('section_a', 'pi_val')
print (doseerpompgpio1)
# update existing value
#config.set('section_a', 'string_val', str(bool_val))


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(doseerpompgpio1,GPIO.OUT)
print 'LED on'
GPIO.output(doseerpompgpio1,GPIO.LOW)
time.sleep(5)
print 'LED off'
GPIO.output(doseerpompgpio1,GPIO.HIGH)

GPIO.cleanup()