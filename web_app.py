from flask import Flask, render_template, request
from configparser import ConfigParser
import _web_functions
import os

class Volumes:
  pump_1_volume = 0
  pump_2_volume = 0
  pump_3_volume = 0
  pump_4_volume = 0

class volume_available:
  volume_available_1 = 0
  volume_available_2 = 0
  volume_available_3 = 0
  volume_available_4 = 0

class volume_available_ml:
  volume_available_1_ml = 0
  volume_available_2_ml = 0
  volume_available_3_ml = 0
  volume_available_4_ml = 0

class Schedules:
  schedule_pump_1 = 0
  schedule_pump_2 = 0
  schedule_pump_3 = 0
  schedule_pump_4 = 0

class volume_reservoirs:
  pump_1_volume_reservoir = 0
  pump_2_volume_reservoir = 0
  pump_3_volume_reservoir = 0
  pump_4_volume_reservoir = 0

class gpio:
  pump_1_gpio = 0
  pump_2_gpio = 0
  pump_3_gpio = 0
  pump_4_gpio = 0

class alias:
  alias_1 = None
  alias_2 = None
  alias_3 = None
  alias_4 = None

class time:
  time = 0  

class mlpersec:
  mlpersec = 0 

app = Flask(__name__)
volumes = Volumes()
volume_available = volume_available()
schedules = Schedules()
volume_reservoirs = volume_reservoirs()
gpio = gpio()
time = time()
mlpersec = mlpersec()
alias = alias()

@app.route('/')
@app.route('/dashboard')
def home():
	_web_functions.get_config_volume_available_ml(volume_available_ml)
	_web_functions.get_config_volume_available(volume_available)
	_web_functions.get_config_alias(alias)
	_web_functions.get_config_volume_reservoirs(volume_reservoirs)
	return render_template('dashboard.html', volume_available_1=volume_available.volume_available_1, volume_available_2=volume_available.volume_available_2, volume_available_3=volume_available.volume_available_3, volume_available_4=volume_available.volume_available_4, vol_res_1=volume_reservoirs.pump_1_volume_reservoir, vol_res_2=volume_reservoirs.pump_2_volume_reservoir, vol_res_3=volume_reservoirs.pump_3_volume_reservoir, vol_res_4=volume_reservoirs.pump_4_volume_reservoir, alias_1=alias.alias_1, alias_2=alias.alias_2, alias_3=alias.alias_3, alias_4=alias.alias_4)

@app.route('/reservoir_available', methods=['GET'])
def reservoir_available():
	_web_functions.get_config_volume_reservoirs(volume_reservoirs)
	_web_functions.get_config_alias(alias)
	_web_functions.get_volume_available_ml_client(volume_available_ml)
	_web_functions.set_config_volume_available_ml(volume_available_ml, volume_reservoirs)
	_web_functions.get_config_volume_available(volume_available)
	return render_template('dashboard.html', volume_available_1=volume_available.volume_available_1, volume_available_2=volume_available.volume_available_2, volume_available_3=volume_available.volume_available_3, volume_available_4=volume_available.volume_available_4, vol_res_1=volume_reservoirs.pump_1_volume_reservoir, vol_res_2=volume_reservoirs.pump_2_volume_reservoir, vol_res_3=volume_reservoirs.pump_3_volume_reservoir, vol_res_4=volume_reservoirs.pump_4_volume_reservoir, alias_1=alias.alias_1, alias_2=alias.alias_2, alias_3=alias.alias_3, alias_4=alias.alias_4)

@app.route('/set')
def set():
	_web_functions.get_config_volume(volumes)
	_web_functions.get_config_schedules(schedules)
	_web_functions.get_config_volume_reservoirs(volume_reservoirs)
	_web_functions.get_config_gpio(gpio)
	_web_functions.get_config_time(time)
	_web_functions.get_config_alias(alias)

	return render_template('index.html', getpump1ml=volumes.pump_1_volume, getpump2ml=volumes.pump_2_volume, getpump3ml=volumes.pump_3_volume, getpump4ml=volumes.pump_4_volume, vol_res_1=volume_reservoirs.pump_1_volume_reservoir, vol_res_2=volume_reservoirs.pump_2_volume_reservoir, vol_res_3=volume_reservoirs.pump_3_volume_reservoir, vol_res_4=volume_reservoirs.pump_4_volume_reservoir, pump_1_gpio=gpio.pump_1_gpio, pump_2_gpio=gpio.pump_2_gpio, pump_3_gpio=gpio.pump_3_gpio, pump_4_gpio=gpio.pump_4_gpio, time=time.time, mlpersec=mlpersec.mlpersec, schedule_pump_1=schedules.schedule_pump_1, schedule_pump_2=schedules.schedule_pump_2, schedule_pump_3=schedules.schedule_pump_3, schedule_pump_4=schedules.schedule_pump_4, alias_1=alias.alias_1, alias_2=alias.alias_2, alias_3=alias.alias_3, alias_4=alias.alias_4)

@app.route('/reservoir', methods=['GET'])
def reservoir():
	_web_functions.get_volume_reservoirs_client(volume_reservoirs)
	_web_functions.set_config_volume_reservoirs(volume_reservoirs)
	return render_template('index.html', vol_res_1=volume_reservoirs.pump_1_volume_reservoir, vol_res_2=volume_reservoirs.pump_2_volume_reservoir, vol_res_3=volume_reservoirs.pump_3_volume_reservoir, vol_res_4=volume_reservoirs.pump_4_volume_reservoir)

@app.route('/gpio', methods=['GET'])
def gpio():
	_web_functions.get_gpio_client(gpio)
	_web_functions.set_config_gpio(gpio)
	return render_template('index.html', pump_1_gpio=gpio.pump_1_gpio, pump_2_gpio=gpio.pump_2_gpio, pump_3_gpio=gpio.pump_3_gpio, pump_4_gpio=gpio.pump_4_gpio)



@app.route('/alias', methods=['GET'])
def alias():
	_web_functions.get_alias_client(alias)
	_web_functions.set_config_alias(alias)
	return render_template('index.html', alias_1=alias.alias_1, alias_2=alias.alias_2, alias_3=alias.alias_3, alias_4=alias.alias_4)



@app.route('/getdosing')
def getdosing():
	_web_functions.get_config_volume(volumes)
	_web_functions.get_config_schedules(schedules)
	_web_functions.get_config_alias(alias)
	return render_template('dosing.html', getpump1ml=volumes.pump_1_volume, getpump2ml=volumes.pump_2_volume, getpump3ml=volumes.pump_3_volume, getpump4ml=volumes.pump_4_volume, schedule_pump_1=schedules.schedule_pump_1, schedule_pump_2=schedules.schedule_pump_2, schedule_pump_3=schedules.schedule_pump_3, schedule_pump_4=schedules.schedule_pump_4, alias_1=alias.alias_1, alias_2=alias.alias_2, alias_3=alias.alias_3, alias_4=alias.alias_4)

@app.route('/setdosing', methods=['GET'])
def setdosing():
	_web_functions.get_volumes_client(volumes)
	_web_functions.get_schedules_client(schedules)
	_web_functions.set_config(volumes, schedules)
	return render_template('dosing.html',getpump1ml=volumes.pump_1_volume, getpump2ml=volumes.pump_2_volume, getpump3ml=volumes.pump_3_volume, getpump4ml=volumes.pump_4_volume, schedule_pump_1=schedules.schedule_pump_1, schedule_pump_2=schedules.schedule_pump_2, schedule_pump_3=schedules.schedule_pump_3, schedule_pump_4=schedules.schedule_pump_4, alias_1=alias.alias_1, alias_2=alias.alias_2, alias_3=alias.alias_3, alias_4=alias.alias_4)

@app.route('/gettime')
def gettime():
	_web_functions.get_config_time(time)
	return render_template('time.html', time=time.time)

@app.route('/settime', methods=['GET'])
def settime():
	_web_functions.get_time_client(time)
	_web_functions.set_config_time(time)
	return render_template('time.html', time=time.time)

@app.route('/getcalibrate')
def getcalibrate():
	_web_functions.get_config_mlpersec(mlpersec)
	_web_functions.get_config_alias(alias)
	return render_template('calibrate.html', mlpersec=mlpersec.mlpersec, alias_1=alias.alias_1, alias_2=alias.alias_2, alias_3=alias.alias_3, alias_4=alias.alias_4)

@app.route('/setcalibrate', methods=['GET'])
def setcalibrate():
	_web_functions.get_mlpersec_client(mlpersec)
	_web_functions.set_config_mlpersec(mlpersec)
	return render_template('calibrate.html', mlpersec=mlpersec.mlpersec, alias_1=alias.alias_1, alias_2=alias.alias_2, alias_3=alias.alias_3, alias_4=alias.alias_4)

@app.route('/test', methods=['GET'])
def testcalibrate():
	pump_test = request.args.get('pump_test')
	test_script = "python ./test.py %s" % (pump_test)
	print (test_script)
	os.system(str(test_script))
	return render_template('calibrate.html', mlpersec=mlpersec.mlpersec, alias_1=alias.alias_1, alias_2=alias.alias_2, alias_3=alias.alias_3, alias_4=alias.alias_4)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=8080)