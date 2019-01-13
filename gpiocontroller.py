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

doseerpompgpio1 = config.getint('gpio', 'doseerpompgpio1')
doseerpompgpio2 = config.getint('gpio', 'doseerpompgpio2')
doseerpompgpio3 = config.getint('gpio', 'doseerpompgpio3')
doseerpompgpio4 = config.getint('gpio', 'doseerpompgpio4')

pomp1ml = config.getint('pomp', 'pomp1ml')
pomp2ml = config.getint('pomp', 'pomp2ml')
pomp3ml = config.getint('pomp', 'pomp3ml')
pomp4ml = config.getint('pomp', 'pomp4ml')

scheduledtime = config.get('time', 'time')

pomp1insec = pomp1ml * mlpersec
pomp2insec = pomp2ml * mlpersec
pomp3insec = pomp3ml * mlpersec
pomp4insec = pomp4ml * mlpersec

#Tijd omzetten om te vergelijken
scheduled = datetime.datetime.strptime(scheduledtime, "%H:%M")
now = datetime.datetime.now()

pomp1 = config.get('pomp', 'pomp1')
pomp2 = config.get('pomp', 'pomp2')
pomp3 = config.get('pomp', 'pomp3')
pomp4 = config.get('pomp', 'pomp4')

weekdag = date.today().weekday()

if str(weekdag) in pomp1 and now.hour == scheduled.hour and now.minute == scheduled.minute:
   	#Pomp1
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(doseerpompgpio1,GPIO.OUT)
	print "Pomp 1 aan voor %d sec om %d ml te pompen." % (pomp1insec,pomp1ml)
	GPIO.output(doseerpompgpio1,GPIO.LOW)
	time.sleep (pomp1insec)
	print 'Pomp 1 uit.'
	GPIO.output(doseerpompgpio1,GPIO.HIGH)
	GPIO.cleanup()
else :
   	print ('Pomp 1 hoeft niet te pompen.')

if str(weekdag) in pomp2 and now.hour == scheduled.hour and now.minute == scheduled.minute:
   	#Pomp2
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(doseerpompgpio2,GPIO.OUT)
	print "Pomp 2 aan voor %d sec om %d ml te pompen." % (pomp2insec,pomp2ml)
	GPIO.output(doseerpompgpio2,GPIO.LOW)
	time.sleep (pomp2insec)
	print 'Pomp 2 uit.'
	GPIO.output(doseerpompgpio2,GPIO.HIGH)
	GPIO.cleanup()
else :
   	print ('Pomp 2 hoeft niet te pompen.')

if str(weekdag) in pomp3 and now.hour == scheduled.hour and now.minute == scheduled.minute:
   	#Pomp3
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(doseerpompgpio3,GPIO.OUT)
	print "Pomp 3 aan voor %d sec om %d ml te pompen." % (pomp3insec,pomp3ml)
	GPIO.output(doseerpompgpio3,GPIO.LOW)
	time.sleep (pomp3insec)
	print 'Pomp 3 uit.'
	GPIO.output(doseerpompgpio3,GPIO.HIGH)
	GPIO.cleanup()
else :
   	print ('Pomp 3 hoeft niet te pompen.')

if str(weekdag) in pomp4 and now.hour == scheduled.hour and now.minute == scheduled.minute:
   	#Pomp4
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(doseerpompgpio4,GPIO.OUT)
	print "Pomp 4 aan voor %d sec om %d ml te pompen." % (pomp4insec,pomp4ml)
	GPIO.output(doseerpompgpio4,GPIO.LOW)
	time.sleep (pomp4insec)
	print 'Pomp 4 uit.'
	GPIO.output(doseerpompgpio4,GPIO.HIGH)
	GPIO.cleanup()
else :
   	print ('Pomp 4 hoeft niet te pompen.')
