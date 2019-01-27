import RPi.GPIO as GPIO
import time, datetime
from configparser import ConfigParser
from datetime import date

# instantiate
config = ConfigParser()

# parse existing file
config.read('settings.ini')

# read values from a section
mlpersec = config.getfloat('mlpersec', 'mlpersec')

pump_1_gpio = config.getint('gpio', 'pump_1_gpio')
pump_2_gpio = config.getint('gpio', 'pump_2_gpio')
pump_3_gpio = config.getint('gpio', 'pump_3_gpio')
pump_4_gpio = config.getint('gpio', 'pump_4_gpio')

reservoir_1 = config.getint('reservoir', 'reservoir1')
reservoir_2 = config.getint('reservoir', 'reservoir2')
reservoir_3 = config.getint('reservoir', 'reservoir3')
reservoir_4 = config.getint('reservoir', 'reservoir4')

pump_1_volume = config.getint('pump', 'pump_1_volume')
pump_2_volume = config.getint('pump', 'pump_2_volume')
pump_3_volume = config.getint('pump', 'pump_3_volume')
pump_4_volume = config.getint('pump', 'pump_4_volume')

scheduledtime = config.get('time', 'time')

pump1insec = pump_1_volume * mlpersec
pump2insec = pump_2_volume * mlpersec
pump3insec = pump_3_volume * mlpersec
pump4insec = pump_4_volume * mlpersec

#Tijd omzetten om te vergelijken
scheduled = datetime.datetime.strptime(scheduledtime, "%H:%M")
now = datetime.datetime.now()

pump1 = config.get('pump', 'schedule_pump_1')
pump2 = config.get('pump', 'schedule_pump_2')
pump3 = config.get('pump', 'schedule_pump_3')
pump4 = config.get('pump', 'schedule_pump_4')

volume_available_1_ml = config.getint('volume_available', 'volume_available_1_ml')
volume_available_2_ml = config.getint('volume_available', 'volume_available_2_ml')
volume_available_3_ml = config.getint('volume_available', 'volume_available_3_ml')
volume_available_4_ml = config.getint('volume_available', 'volume_available_4_ml')

weekdag = date.today().weekday()

if str(weekdag) in pump1 and now.hour == scheduled.hour and now.minute == scheduled.minute:
   	#pump1
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(pump_1_gpio,GPIO.OUT)
	print "pump 1 aan voor %d sec om %d ml te pumpen." % (pump1insec,pump_1_volume)
	GPIO.output(pump_1_gpio,GPIO.LOW)
	time.sleep (pump1insec)
	print 'pump 1 uit.'
	GPIO.output(pump_1_gpio,GPIO.HIGH)
	GPIO.cleanup()
	volume_available_1_ml_new = volume_available_1_ml - pump_1_volume
	volume_available_1 = 100 * volume_available_1_ml_new / reservoir_1
  	config = ConfigParser()
  	config.read('settings.ini')
  	config.set('volume_available', 'volume_available_1_ml', str(volume_available_1_ml_new))
  	config.set('volume_available', 'volume_available_1', str(volume_available_1))
	with open('settings.ini', 'w') as configfile:
		config.write(configfile)

else :
   	print ('pump 1 hoeft niet te pumpen.')

if str(weekdag) in pump2 and now.hour == scheduled.hour and now.minute == scheduled.minute:
   	#pump2
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(pump_2_gpio,GPIO.OUT)
	print "pump 2 aan voor %d sec om %d ml te pumpen." % (pump2insec,pump_2_volume)
	GPIO.output(pump_2_gpio,GPIO.LOW)
	time.sleep (pump2insec)
	print 'pump 2 uit.'
	GPIO.output(pump_2_gpio,GPIO.HIGH)
	GPIO.cleanup()
	volume_available_2_ml_new = volume_available_2_ml - pump_2_volume
	volume_available_2 = 100 * volume_available_2_ml_new / reservoir_2
  	config = ConfigParser()
  	config.read('settings.ini')
  	config.set('volume_available', 'volume_available_2_ml', str(volume_available_2_ml_new))
  	config.set('volume_available', 'volume_available_2', str(volume_available_2))
	with open('settings.ini', 'w') as configfile:
		config.write(configfile)
else :
   	print ('pump 2 hoeft niet te pumpen.')

if str(weekdag) in pump3 and now.hour == scheduled.hour and now.minute == scheduled.minute:
   	#pump3
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(pump_3_gpio,GPIO.OUT)
	print "pump 3 aan voor %d sec om %d ml te pumpen." % (pump3insec,pump_3_volume)
	GPIO.output(pump_3_gpio,GPIO.LOW)
	time.sleep (pump3insec)
	print 'pump 3 uit.'
	GPIO.output(pump_3_gpio,GPIO.HIGH)
	GPIO.cleanup()
	volume_available_3_ml_new = volume_available_3_ml - pump_3_volume
	volume_available_3 = 100 * volume_available_3_ml_new / reservoir_3
  	config = ConfigParser()
  	config.read('settings.ini')
  	config.set('volume_available', 'volume_available_3_ml', str(volume_available_3_ml_new))
  	config.set('volume_available', 'volume_available_3', str(volume_available_3))
	with open('settings.ini', 'w') as configfile:
		config.write(configfile)
else :
   	print ('pump 3 hoeft niet te pumpen.')

if str(weekdag) in pump4 and now.hour == scheduled.hour and now.minute == scheduled.minute:
   	#pump4
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(pump_4_gpio,GPIO.OUT)
	print "pump 4 aan voor %d sec om %d ml te pumpen." % (pump4insec,pump_4_volume)
	GPIO.output(pump_4_gpio,GPIO.LOW)
	time.sleep (pump4insec)
	print 'pump 4 uit.'
	GPIO.output(pump_4_gpio,GPIO.HIGH)
	GPIO.cleanup()
	volume_available_4_ml_new = volume_available_4_ml - pump_4_volume
	volume_available_4 = 100 * volume_available_4_ml_new / reservoir_4
  	config = ConfigParser()
  	config.read('settings.ini')
  	config.set('volume_available', 'volume_available_4_ml', str(volume_available_4_ml_new))
  	config.set('volume_available', 'volume_available_4', str(volume_available_4))
	with open('settings.ini', 'w') as configfile:
		config.write(configfile)
else :
   	print ('pump 4 hoeft niet te pumpen.')
