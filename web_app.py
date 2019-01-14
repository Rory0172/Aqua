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

class volume_reservoirs:
  pomp_1_volume_reservoir = 0
  pomp_2_volume_reservoir = 0
  pomp_3_volume_reservoir = 0
  pomp_4_volume_reservoir = 0

class gpio:
  pomp_1_gpio = 0
  pomp_2_gpio = 0
  pomp_3_gpio = 0
  pomp_4_gpio = 0

app = Flask(__name__)
volumes = Volumes()
schedules = Schedules()
volume_reservoirs = volume_reservoirs()
gpio = gpio()

@app.route('/')
def home():
	_web_functions.get_config_volume(volumes)
	_web_functions.get_config_volume_reservoirs(volume_reservoirs)
	_web_functions.get_config_gpio(gpio)
	return render_template('index.html',getpomp1ml=volumes.pomp_1_volume, getpomp2ml=volumes.pomp_2_volume, getpomp3ml=volumes.pomp_3_volume, getpomp4ml=volumes.pomp_4_volume, vol_res_1=volume_reservoirs.pomp_1_volume_reservoir, vol_res_2=volume_reservoirs.pomp_2_volume_reservoir, vol_res_3=volume_reservoirs.pomp_3_volume_reservoir, vol_res_4=volume_reservoirs.pomp_4_volume_reservoir, pomp_1_gpio=gpio.pomp_1_gpio, pomp_2_gpio=gpio.pomp_2_gpio, pomp_3_gpio=gpio.pomp_3_gpio, pomp_4_gpio=gpio.pomp_4_gpio)

@app.route('/setup', methods=['GET'])			#URL to INI config
def setup():
	_web_functions.get_volumes_client(volumes)
	_web_functions.get_schedules_client(schedules)
	_web_functions.set_config(volumes, schedules)
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
	_web_functions.get_volume_reservoirs_client(volume_reservoirs)
	_web_functions.set_config_volume_reservoirs(volume_reservoirs)
	return render_template('index.html', vol_res_1=volume_reservoirs.pomp_1_volume_reservoir, vol_res_2=volume_reservoirs.pomp_2_volume_reservoir, vol_res_3=volume_reservoirs.pomp_3_volume_reservoir, vol_res_4=volume_reservoirs.pomp_4_volume_reservoir)

@app.route('/gpio', methods=['GET'])			#URL to INI config
def gpio():
	_web_functions.get_gpio_client(gpio)
	_web_functions.set_config_gpio(gpio)
	return render_template('index.html', pomp_1_gpio=gpio.pomp_1_gpio, pomp_2_gpio=gpio.pomp_2_gpio, pomp_3_gpio=gpio.pomp_3_gpio, pomp_4_gpio=gpio.pomp_4_gpio)

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

@app.route('/dashboard')
def dashboard():
   return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=8080)
