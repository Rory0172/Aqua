from flask import Flask, render_template, request, url_for
from configparser import ConfigParser


app = Flask(__name__)

@app.route('/')
def hello():
   return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    print(username)
    password = request.args.get('password')
    print(password)
    return render_template('index.html')

@app.route('/pomp', methods=['GET'])			#URL to INI config
def pomp():
	#Get info from URL
	pomp1ml = request.args.get('pomp1ml')
	pomp2ml = request.args.get('pomp2ml')
	pomp3ml = request.args.get('pomp3ml')
	pomp4ml = request.args.get('pomp4ml')

	pomp1maandag = request.args.get('pomp1maandag')
	pomp1dinsdag = request.args.get('pomp1dinsdag')
	pomp1woensdag = request.args.get('pomp1woensdag')
	pomp1donderdag = request.args.get('pomp1donderdag')
	pomp1vrijdag = request.args.get('pomp1vrijdag')
	pomp1zaterdag = request.args.get('pomp1zaterdag')
	pomp1zondag= request.args.get('pomp1zondag')

	pomp2maandag = request.args.get('pomp2maandag')
	pomp2dinsdag = request.args.get('pomp2dinsdag')
	pomp2woensdag = request.args.get('pomp2woensdag')
	pomp2donderdag = request.args.get('pomp2donderdag')
	pomp2vrijdag = request.args.get('pomp2vrijdag')
	pomp2zaterdag = request.args.get('pomp2zaterdag')
	pomp2zondag= request.args.get('pomp2zondag')

	pomp3maandag = request.args.get('pomp3maandag')
	pomp3dinsdag = request.args.get('pomp3dinsdag')
	pomp3woensdag = request.args.get('pomp3woensdag')
	pomp3donderdag = request.args.get('pomp3donderdag')
	pomp3vrijdag = request.args.get('pomp3vrijdag')
	pomp3zaterdag = request.args.get('pomp3zaterdag')
	pomp3zondag= request.args.get('pomp3zondag')

	pomp4maandag = request.args.get('pomp4maandag')
	pomp4dinsdag = request.args.get('pomp4dinsdag')
	pomp4woensdag = request.args.get('pomp4woensdag')
	pomp4donderdag = request.args.get('pomp4donderdag')
	pomp4vrijdag = request.args.get('pomp4vrijdag')
	pomp4zaterdag = request.args.get('pomp4zaterdag')
	pomp4zondag= request.args.get('pomp4zondag')

	pomp1 = str(pomp1maandag) + str(pomp1dinsdag) + str(pomp1woensdag) + str(pomp1donderdag) + str(pomp1vrijdag) + str(pomp1zaterdag) + str(pomp1zondag)
	pomp1clean = pomp1.replace('None', '')
	pomp2 = str(pomp2maandag) + str(pomp2dinsdag) + str(pomp2woensdag) + str(pomp2donderdag) + str(pomp2vrijdag) + str(pomp2zaterdag) + str(pomp2zondag)
	pomp2clean = pomp2.replace('None', '')
	pomp3 = str(pomp3maandag) + str(pomp3dinsdag) + str(pomp3woensdag) + str(pomp3donderdag) + str(pomp3vrijdag) + str(pomp3zaterdag) + str(pomp3zondag)
	pomp3clean = pomp3.replace('None', '')
	pomp4 = str(pomp4maandag) + str(pomp4dinsdag) + str(pomp4woensdag) + str(pomp4donderdag) + str(pomp4vrijdag) + str(pomp4zaterdag) + str(pomp4zondag)
	pomp4clean = pomp4.replace('None', '')

	print (pomp1maandag)

	config = ConfigParser(allow_no_value=True)

# parse existing file
	config.read('settings.ini')

	#Get info from existing config file
	getpomp1ml = config.get('pomp', 'pomp1ml')
	getpomp2ml = config.get('pomp', 'pomp2ml')
	getpomp3ml = config.get('pomp', 'pomp3ml')
	getpomp4ml = config.get('pomp', 'pomp4ml')

	config.set('pomp', 'pomp1ml', str(pomp1ml))
	config.set('pomp', 'pomp2ml', str(pomp2ml))
	config.set('pomp', 'pomp3ml', str(pomp3ml))
	config.set('pomp', 'pomp4ml', str(pomp4ml))

	config.set('pomp', 'pomp1', str(pomp1clean))
	config.set('pomp', 'pomp2', str(pomp2clean))
	config.set('pomp', 'pomp3', str(pomp3clean))
	config.set('pomp', 'pomp4', str(pomp4clean))

	with open('settings.ini', 'w') as configfile:
		config.write(configfile)
		return render_template('index.html', getpomp2ml=getpomp2ml, getpomp3ml=getpomp3ml, getpomp4ml=getpomp4ml)

@app.route('/mlpersec', methods=['GET'])			#URL to INI config
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

@app.route('/dashboard')
def dashboard():
   return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=8080)