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

pomp_1_gpio = config.getint('gpio', 'pomp_1_gpio')
pomp_2_gpio = config.getint('gpio', 'pomp_2_gpio')
pomp_3_gpio = config.getint('gpio', 'pomp_3_gpio')
pomp_4_gpio = config.getint('gpio', 'pomp_4_gpio')

reservoir_1 = config.getint('reservoir', 'reservoir1')
reservoir_2 = config.getint('reservoir', 'reservoir2')
reservoir_3 = config.getint('reservoir', 'reservoir3')
reservoir_4 = config.getint('reservoir', 'reservoir4')

pomp_1_volume = config.getint('pomp', 'pomp_1_volume')
pomp_2_volume = config.getint('pomp', 'pomp_2_volume')
pomp_3_volume = config.getint('pomp', 'pomp_3_volume')
pomp_4_volume = config.getint('pomp', 'pomp_4_volume')

scheduledtime = config.get('time', 'time')

pomp1insec = pomp_1_volume * mlpersec
pomp2insec = pomp_2_volume * mlpersec
pomp3insec = pomp_3_volume * mlpersec
pomp4insec = pomp_4_volume * mlpersec

#Tijd omzetten om te vergelijken
scheduled = datetime.datetime.strptime(scheduledtime, "%H:%M")
now = datetime.datetime.now()

pomp1 = config.get('pomp', 'schedule_pomp_1')
pomp2 = config.get('pomp', 'schedule_pomp_2')
pomp3 = config.get('pomp', 'schedule_pomp_3')
pomp4 = config.get('pomp', 'schedule_pomp_4')

volume_available_1_ml = config.getint('volume_available', 'volume_available_1_ml')
volume_available_2_ml = config.getint('volume_available', 'volume_available_2_ml')
volume_available_3_ml = config.getint('volume_available', 'volume_available_3_ml')
volume_available_4_ml = config.getint('volume_available', 'volume_available_4_ml')

weekdag = date.today().weekday()

if str(weekdag) in pomp1 and now.hour == scheduled.hour and now.minute == scheduled.minute:
   	#Pomp1
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(pomp_1_gpio,GPIO.OUT)
	print "Pomp 1 aan voor %d sec om %d ml te pompen." % (pomp1insec,pomp_1_volume)
	GPIO.output(pomp_1_gpio,GPIO.LOW)
	time.sleep (pomp1insec)
	print 'Pomp 1 uit.'
	GPIO.output(pomp_1_gpio,GPIO.HIGH)
	GPIO.cleanup()
	volume_available_1_ml_new = volume_available_1_ml - pomp_1_volume
	volume_available_1 = 100 * volume_available_1_ml_new / reservoir_1
  	config = ConfigParser()
  	config.read('settings.ini')
  	config.set('volume_available', 'volume_available_1_ml', str(volume_available_1_ml_new))
  	config.set('volume_available', 'volume_available_1', str(volume_available_1))
	with open('settings.ini', 'w') as configfile:
		config.write(configfile)

else :
   	print ('Pomp 1 hoeft niet te pompen.')

if str(weekdag) in pomp2 and now.hour == scheduled.hour and now.minute == scheduled.minute:
   	#Pomp2
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(pomp_2_gpio,GPIO.OUT)
	print "Pomp 2 aan voor %d sec om %d ml te pompen." % (pomp2insec,pomp_2_volume)
	GPIO.output(pomp_2_gpio,GPIO.LOW)
	time.sleep (pomp2insec)
	print 'Pomp 2 uit.'
	GPIO.output(pomp_2_gpio,GPIO.HIGH)
	GPIO.cleanup()
	volume_available_2_ml_new = volume_available_2_ml - pomp_2_volume
	volume_available_2 = 100 * volume_available_2_ml_new / reservoir_2
  	config = ConfigParser()
  	config.read('settings.ini')
  	config.set('volume_available', 'volume_available_2_ml', str(volume_available_2_ml_new))
  	config.set('volume_available', 'volume_available_2', str(volume_available_2))
	with open('settings.ini', 'w') as configfile:
		config.write(configfile)
else :
   	print ('Pomp 2 hoeft niet te pompen.')

if str(weekdag) in pomp3 and now.hour == scheduled.hour and now.minute == scheduled.minute:
   	#Pomp3
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(pomp_3_gpio,GPIO.OUT)
	print "Pomp 3 aan voor %d sec om %d ml te pompen." % (pomp3insec,pomp_3_volume)
	GPIO.output(pomp_3_gpio,GPIO.LOW)
	time.sleep (pomp3insec)
	print 'Pomp 3 uit.'
	GPIO.output(pomp_3_gpio,GPIO.HIGH)
	GPIO.cleanup()
	volume_available_3_ml_new = volume_available_3_ml - pomp_3_volume
	volume_available_3 = 100 * volume_available_3_ml_new / reservoir_3
  	config = ConfigParser()
  	config.read('settings.ini')
  	config.set('volume_available', 'volume_available_3_ml', str(volume_available_3_ml_new))
  	config.set('volume_available', 'volume_available_3', str(volume_available_3))
	with open('settings.ini', 'w') as configfile:
		config.write(configfile)
else :
   	print ('Pomp 3 hoeft niet te pompen.')

if str(weekdag) in pomp4 and now.hour == scheduled.hour and now.minute == scheduled.minute:
   	#Pomp4
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(pomp_4_gpio,GPIO.OUT)
	print "Pomp 4 aan voor %d sec om %d ml te pompen." % (pomp4insec,pomp_4_volume)
	GPIO.output(pomp_4_gpio,GPIO.LOW)
	time.sleep (pomp4insec)
	print 'Pomp 4 uit.'
	GPIO.output(pomp_4_gpio,GPIO.HIGH)
	GPIO.cleanup()
	volume_available_4_ml_new = volume_available_4_ml - pomp_4_volume
	volume_available_4 = 100 * volume_available_4_ml_new / reservoir_4
  	config = ConfigParser()
  	config.read('settings.ini')
  	config.set('volume_available', 'volume_available_4_ml', str(volume_available_4_ml_new))
  	config.set('volume_available', 'volume_available_4', str(volume_available_4))
	with open('settings.ini', 'w') as configfile:
		config.write(configfile)
else :
   	print ('Pomp 4 hoeft niet te pompen.')
