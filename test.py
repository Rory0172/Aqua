import RPi.GPIO as GPIO
import sys
import time
from configparser import ConfigParser

gpio_pins = ['pump_1_gpio','pump_2_gpio', 'pump_3_gpio', 'pump_4_gpio']
pump_names = ['macro voeding', 'micro voeding', 'ijzer']

def test_run(pump_number):
  pump_number = int(pump_number)
  config = ConfigParser()
  config.read('./settings.ini')

  flow_rate = config.getfloat('mlpersec', 'mlpersec')
  pump_duration = 5 * flow_rate

  pump_pin = config.getint('gpio', gpio_pins[pump_number])
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(pump_pin,GPIO.OUT)
  print"pump ",pump_names[pump_number]," aan voor ",pump_duration," sec om 5 ml te pumpen."
  GPIO.output(pump_pin,GPIO.LOW)
  time.sleep (pump_duration)
  print"pump ",pump_names[pump_number]," uit."
  GPIO.output(pump_pin,GPIO.HIGH)


  pump_numbers = [0,1,2,3]

  for pump_number in pump_numbers:
    if pump_number == 0:
      volume_available_1_ml_new = volume_available_1_ml - 5
      volume_available = int(100 * int(volume_available_1_ml) / int(pump_1_volume_reservoir))
      config.set('volume_available', 'volume_available_1_ml', str(volume_available_1_ml_new))
      config.set('volume_available', 'volume_available_1', str(volume_available))

    elif pump_number == 1:
      volume_available = int(100 * int(volume_available_2_ml) / int(volume_reservoirs.pump_2_volume_reservoir))
      config.set('volume_available', 'volume_available_2_ml', str(volume_available_ml.volume_available_2_ml))
      config.set('volume_available', 'volume_available_2', str(volume_available))

    elif pump_number == 2:
      volume_available = int(100 * int(volume_available_3_ml) / int(volume_reservoirs.pump_3_volume_reservoir))
      config.set('volume_available', 'volume_available_3_ml', str(volume_available_ml.volume_available_3_ml))
      config.set('volume_available', 'volume_available_3', str(volume_available))

    elif pump_number == 3:
      volume_available = int(100 * int(volume_available_ml.volume_available_4_ml) / int(volume_reservoirs.pump_4_volume_reservoir))
      config.set('volume_available', 'volume_available_4_ml', str(volume_available_ml.volume_available_4_ml))
      config.set('volume_available', 'volume_available_4', str(volume_available))

if __name__ == "__main__":
  pump_number = sys.argv[1]
  test_run(pump_number)