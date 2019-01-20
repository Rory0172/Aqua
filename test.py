import RPi.GPIO as GPIO
import sys
import time
from configparser import ConfigParser

gpio_pins = ['pomp_1_gpio','pomp_2_gpio', 'pomp_3_gpio', 'pomp_4_gpio']
pomp_names = ['macro voeding', 'micro voeding', 'ijzer']

def test_run(pomp_number):
  pomp_number = int(pomp_number)
  config = ConfigParser()
  config.read('./settings.ini')

  flow_rate = config.getfloat('mlpersec', 'mlpersec')
  pump_duration = 5 * flow_rate

  pomp_pin = config.getint('gpio', gpio_pins[pomp_number])
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(pomp_pin,GPIO.OUT)
  print 'Pomp {pomp_names[pomp_number]} aan voor %d sec om 5 ml te pompen.' % (pump_duration)
  GPIO.output(pomp_pin,GPIO.LOW)
  time.sleep (pump_duration)
  print 'Pomp {pomp_names[pomp_number]} uit.'
  GPIO.output(pomp_pin,GPIO.HIGH)



if __name__ == "__main__":
  pomp_number = sys.argv[1]
  test_run(pomp_number)