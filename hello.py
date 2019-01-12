from flask import Flask, render_template, request
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
	
	config = ConfigParser()

# parse existing file
	config.read('settings.ini')
	config.set('pomp', 'pomp1ml', str(pomp1ml))
	config.set('pomp', 'pomp2ml', str(pomp2ml))
	config.set('pomp', 'pomp3ml', str(pomp3ml))
	config.set('pomp', 'pomp4ml', str(pomp4ml))

	config.set('pomp', 'pomp1maandag', str(pomp1maandag))
	config.set('pomp', 'pomp1dinsdag', str(pomp1dinsdag))
	config.set('pomp', 'pomp1woensdag', str(pomp1woensdag))
	config.set('pomp', 'pomp1donderdag', str(pomp1donderdag))
	config.set('pomp', 'pomp1vrijdag', str(pomp1vrijdag))
	config.set('pomp', 'pomp1zaterdag', str(pomp1zaterdag))
	config.set('pomp', 'pomp1zondag', str(pomp1zondag))

	config.set('pomp', 'pomp2maandag', str(pomp2maandag))
	config.set('pomp', 'pomp2dinsdag', str(pomp2dinsdag))
	config.set('pomp', 'pomp2woensdag', str(pomp2woensdag))
	config.set('pomp', 'pomp2donderdag', str(pomp2donderdag))
	config.set('pomp', 'pomp2vrijdag', str(pomp2vrijdag))
	config.set('pomp', 'pomp2zaterdag', str(pomp2zaterdag))
	config.set('pomp', 'pomp2zondag', str(pomp2zondag))

	config.set('pomp', 'pomp3maandag', str(pomp3maandag))
	config.set('pomp', 'pomp3dinsdag', str(pomp3dinsdag))
	config.set('pomp', 'pomp3woensdag', str(pomp3woensdag))
	config.set('pomp', 'pomp3donderdag', str(pomp3donderdag))
	config.set('pomp', 'pomp3vrijdag', str(pomp3vrijdag))
	config.set('pomp', 'pomp3zaterdag', str(pomp3zaterdag))
	config.set('pomp', 'pomp3zondag', str(pomp3zondag))

	config.set('pomp', 'pomp4maandag', str(pomp4maandag))
	config.set('pomp', 'pomp4dinsdag', str(pomp4dinsdag))
	config.set('pomp', 'pomp4woensdag', str(pomp4woensdag))
	config.set('pomp', 'pomp4donderdag', str(pomp4donderdag))
	config.set('pomp', 'pomp4vrijdag', str(pomp4vrijdag))
	config.set('pomp', 'pomp4zaterdag', str(pomp4zaterdag))
	config.set('pomp', 'pomp4zondag', str(pomp4zondag))

	with open('settings.ini', 'w') as configfile:
		config.write(configfile)
		return render_template('index.html')

@app.route('/mlpersec', methods=['GET'])			#URL to INI config
def mlpersec():
	mlpersec = request.args.get('mlpersec')
	
	config = ConfigParser()
# parse existing file
	config.read('settings.ini')
	config.set('mlpersec', 'mlpersec', str(mlpersec))

	with open('settings.ini', 'w') as configfile1:
		config.write(configfile1)
		return render_template('index.html')

@app.route('/reservoir', methods=['GET'])			#URL to INI config
def reservoir():
	reservoir1 = request.args.get('reservoir1')
	reservoir2 = request.args.get('reservoir2')
	reservoir3 = request.args.get('reservoir3')
	reservoir4 = request.args.get('reservoir4')

	config = ConfigParser()
# parse existing file
	config.read('settings.ini')
	config.set('reservoir', 'reservoir1', str(reservoir1))
	config.set('reservoir', 'reservoir2', str(reservoir2))
	config.set('reservoir', 'reservoir3', str(reservoir3))
	config.set('reservoir', 'reservoir4', str(reservoir4))

	with open('settings.ini', 'w') as configfile2:
		config.write(configfile2)
		return render_template('index.html')

@app.route('/gpio', methods=['GET'])			#URL to INI config
def gpio():
	doseerpompgpio1 = request.args.get('doseerpompgpio1')
	doseerpompgpio2 = request.args.get('doseerpompgpio2')
	doseerpompgpio3 = request.args.get('doseerpompgpio3')
	doseerpompgpio4 = request.args.get('doseerpompgpio4')

	config = ConfigParser()
# parse existing file
	config.read('settings.ini')
	config.set('gpio', 'doseerpompgpio1', str(doseerpompgpio1))
	config.set('gpio', 'doseerpompgpio2', str(doseerpompgpio2))
	config.set('gpio', 'doseerpompgpio3', str(doseerpompgpio3))
	config.set('gpio', 'doseerpompgpio4', str(doseerpompgpio4))

	with open('settings.ini', 'w') as configfile2:
		config.write(configfile2)
		return render_template('index.html')

if __name__ == '__main__':
    app.run()