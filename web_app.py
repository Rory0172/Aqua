from flask import Flask, render_template, request
from configparser import ConfigParser
import _web_functions

class Volumes:
  pomp_1_volume = 0
  pomp_2_volume = 0
  pomp_3_volume = 0
  pomp_4_volume = 0

class Schedules:
	schedule_pomp_1 = 0
	schedule_pomp_2 = 0
	schedule_pomp_3 = 0
	schedule_pomp_4 = 0

app = Flask(__name__)
volumes = Volumes()
schedules = Schedules()

@app.route('/')
def home():
	_web_functions.get_config(volumes)
	return render_template('index.html',getpomp1ml=volumes.pomp_1_volume, getpomp2ml=volumes.pomp_2_volume, getpomp3ml=volumes.pomp_3_volume, getpomp4ml=volumes.pomp_4_volume)

@app.route('/setup', methods=['GET'])			#URL to INI config
def setup():
	_web_functions.get_volumes_client(volumes)
	print(volumes.pomp_1_volume)
	# _web_functions.get_schedules_client(schedules)
	_web_functions.set_config(volumes)
	return render_template('index.html',getpomp1ml=volumes.pomp_1_volume, getpomp2ml=volumes.pomp_2_volume, getpomp3ml=volumes.pomp_3_volume, getpomp4ml=volumes.pomp_4_volume)

@app.route('/;', methods=['GET'])			#URL to INI config
def mlpersec():
	mlpersec = request.args.get('mlpersec')

	config = ConfigParser(allow_no_value=True)
# parse existing file
	config.read('settings.ini')
	config.set('mlpersec', 'mlpersec', str(mlpersec))

	with open('settings.ini', 'w') as configfile:
		config.write(configfile)
		return render_template('index.html')

@app.route('/reservoir', methods=['GET'])			#URL to INI config
def reservoir():
	reservoir1 = request.args.get('reservoir1')
	reservoir2 = request.args.get('reservoir2')
	reservoir3 = request.args.get('reservoir3')
	reservoir4 = request.args.get('reservoir4')

	config = ConfigParser(allow_no_value=True)
# parse existing file
	config.read('settings.ini')
	config.set('reservoir', 'reservoir1', str(reservoir1))
	config.set('reservoir', 'reservoir2', str(reservoir2))
	config.set('reservoir', 'reservoir3', str(reservoir3))
	config.set('reservoir', 'reservoir4', str(reservoir4))

	with open('settings.ini', 'w') as configfile:
		config.write(configfile)
		return render_template('index.html')

@app.route('/gpio', methods=['GET'])			#URL to INI config
def gpio():
	doseerpompgpio1 = request.args.get('doseerpompgpio1')
	doseerpompgpio2 = request.args.get('doseerpompgpio2')
	doseerpompgpio3 = request.args.get('doseerpompgpio3')
	doseerpompgpio4 = request.args.get('doseerpompgpio4')

	config = ConfigParser(allow_no_value=True)
# parse existing file
	config.read('settings.ini')
	config.set('gpio', 'doseerpompgpio1', str(doseerpompgpio1))
	config.set('gpio', 'doseerpompgpio2', str(doseerpompgpio2))
	config.set('gpio', 'doseerpompgpio3', str(doseerpompgpio3))
	config.set('gpio', 'doseerpompgpio4', str(doseerpompgpio4))

	with open('settings.ini', 'w') as configfile:
		config.write(configfile)
		return render_template('index.html')

@app.route('/time', methods=['GET'])			#URL to INI config
def time():
	time = request.args.get('time')

	config = ConfigParser()
# parse existing file
	config.read('settings.ini')
	config.set('time', 'time', str(time))

	with open('settings.ini', 'w') as configfile:
		config.write(configfile)
		return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=8080)
