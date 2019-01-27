import RPi.GPIO as GPIO
import sys
import time
from configparser import ConfigParser

gpio_pins = ['pump_1_gpio','pump_2_gpio', 'pump_3_gpio', 'pump_4_gpio']
pump_names = ['alias_1', 'alias_2', 'alias_3', 'alias_4']

def test_run(pump_number):
  pump_number = int(pump_number)
  config = ConfigParser()
  config.read('./settings.ini')

  flow_rate = config.getfloat('mlpersec', 'mlpersec')
  pump_duration = 4 * flow_rate

  pump_pin = config.getint('gpio', gpio_pins[pump_number])
  pump_alias = config.get('alias', pump_names[pump_number])
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(pump_pin,GPIO.OUT)
  print"pump ", pump_alias," aan voor ",pump_duration," sec om 5 ml te pumpen."
  GPIO.output(pump_pin,GPIO.LOW)
  time.sleep (pump_duration)
  print"pump ", pump_alias," uit."
  GPIO.output(pump_pin,GPIO.HIGH)

if __name__ == "__main__":
  pump_number = sys.argv[1]
  test_run(pump_number)