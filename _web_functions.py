from configparser import ConfigParser
from flask import request

def get_volumes_client(self):
  self.pomp_1_volume = request.args.get('pomp1ml')
  self.pomp_2_volume = request.args.get('pomp2ml')
  self.pomp_3_volume = request.args.get('pomp3ml')
  self.pomp_4_volume = request.args.get('pomp4ml')
  return self

def get_schedules_client(self):
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

  self.schedule_pomp_1 = (str(pomp1maandag) + str(pomp1dinsdag) + str(pomp1woensdag) + str(pomp1donderdag) + str(pomp1vrijdag) + str(pomp1zaterdag) + str(pomp1zondag)).replace("None", '')
  self.schedule_pomp_2 = (str(pomp2maandag) + str(pomp2dinsdag) + str(pomp2woensdag) + str(pomp2donderdag) + str(pomp2vrijdag) + str(pomp2zaterdag) + str(pomp2zondag)).replace("None", '')
  self.schedule_pomp_3 = (str(pomp3maandag) + str(pomp3dinsdag) + str(pomp3woensdag) + str(pomp3donderdag) + str(pomp3vrijdag) + str(pomp3zaterdag) + str(pomp3zondag)).replace('None', '')
  self.schedule_pomp_4 = (str(pomp4maandag) + str(pomp4dinsdag) + str(pomp4woensdag) + str(pomp4donderdag) + str(pomp4vrijdag) + str(pomp4zaterdag) + str(pomp4zondag)).replace('None', '')
  return self

def get_volume_reservoirs_client(self):
  self.pomp_1_volume_reservoir = request.args.get('reservoir1')
  self.pomp_2_volume_reservoir = request.args.get('reservoir2')
  self.pomp_3_volume_reservoir = request.args.get('reservoir3')
  self.pomp_4_volume_reservoir = request.args.get('reservoir4')
  return self

def get_gpio_client(self):
  self.pomp_1_gpio = request.args.get('pomp1gpio')
  self.pomp_2_gpio = request.args.get('pomp2gpio')
  self.pomp_3_gpio = request.args.get('pomp3gpio')
  self.pomp_4_gpio = request.args.get('pomp4gpio')
  return self

def get_time_client(self):
  self.time = request.args.get('time')
  return self

def get_mlpersec_client(self):
  self.mlpersec = request.args.get('mlpersec')
  return self

def get_config_volume(self):
  config = ConfigParser(allow_no_value=True)
  config.read('settings.ini')
  self.pomp_1_volume = config.get('pomp', 'pomp_1_volume')
  self.pomp_2_volume = config.get('pomp', 'pomp_2_volume')
  self.pomp_3_volume = config.get('pomp', 'pomp_3_volume')
  self.pomp_4_volume = config.get('pomp', 'pomp_4_volume')
  return self 

def get_config_schedules(self):
  config = ConfigParser(allow_no_value=True)
  config.read('settings.ini')
  self.schedule_pomp_1 = config.get('pomp', 'schedule_pomp_1')
  self.schedule_pomp_2 = config.get('pomp', 'schedule_pomp_2')
  self.schedule_pomp_3 = config.get('pomp', 'schedule_pomp_3')
  self.schedule_pomp_4 = config.get('pomp', 'schedule_pomp_4')
  return self 

def get_config_volume_reservoirs(self):
  config = ConfigParser(allow_no_value=True)
  config.read('settings.ini')
  self.pomp_1_volume_reservoir = config.get('reservoir', 'reservoir1')
  self.pomp_2_volume_reservoir = config.get('reservoir', 'reservoir2')
  self.pomp_3_volume_reservoir = config.get('reservoir', 'reservoir3')
  self.pomp_4_volume_reservoir = config.get('reservoir', 'reservoir4')
  return self

def get_config_gpio(self):
  config = ConfigParser(allow_no_value=True)
  config.read('settings.ini')
  self.pomp_1_gpio = config.get('gpio', 'pomp_1_gpio')
  self.pomp_2_gpio = config.get('gpio', 'pomp_2_gpio')
  self.pomp_3_gpio = config.get('gpio', 'pomp_3_gpio')
  self.pomp_4_gpio = config.get('gpio', 'pomp_4_gpio')
  return self

def get_config_time(self):
  config = ConfigParser(allow_no_value=True)
  config.read('settings.ini')
  self.time = config.get('time', 'time')
  return self

def get_config_mlpersec(self):
  config = ConfigParser(allow_no_value=True)
  config.read('settings.ini')
  self.mlpersec = config.get('mlpersec', 'mlpersec')
  return self

def set_config(volumes, schedules):
  config = ConfigParser()
  config.read('settings.ini')
  config.set('pomp', 'pomp_1_volume', str(volumes.pomp_1_volume))
  config.set('pomp', 'pomp_2_volume', str(volumes.pomp_2_volume))
  config.set('pomp', 'pomp_3_volume', str(volumes.pomp_3_volume))
  config.set('pomp', 'pomp_4_volume', str(volumes.pomp_4_volume))
  config.set('pomp', 'schedule_pomp_1', str(schedules.schedule_pomp_1))
  config.set('pomp', 'schedule_pomp_2', str(schedules.schedule_pomp_2))
  config.set('pomp', 'schedule_pomp_3', str(schedules.schedule_pomp_3))
  config.set('pomp', 'schedule_pomp_4', str(schedules.schedule_pomp_4))

  with open('settings.ini', 'w') as configfile:
    config.write(configfile)
  return volumes, schedules

def set_config_volume_reservoirs(volume_reservoirs):
  config = ConfigParser()
  config.read('settings.ini')
  config.set('reservoir', 'reservoir1', str(volume_reservoirs.pomp_1_volume_reservoir))
  config.set('reservoir', 'reservoir2', str(volume_reservoirs.pomp_2_volume_reservoir))
  config.set('reservoir', 'reservoir3', str(volume_reservoirs.pomp_3_volume_reservoir))
  config.set('reservoir', 'reservoir4', str(volume_reservoirs.pomp_4_volume_reservoir))
  
  with open('settings.ini', 'w') as configfile:
    config.write(configfile)
  return volume_reservoirs

def set_config_gpio(gpio):
  config = ConfigParser()
  config.read('settings.ini')
  config.set('gpio', 'pomp_1_gpio', str(gpio.pomp_1_gpio))
  config.set('gpio', 'pomp_2_gpio', str(gpio.pomp_2_gpio))
  config.set('gpio', 'pomp_3_gpio', str(gpio.pomp_3_gpio))
  config.set('gpio', 'pomp_4_gpio', str(gpio.pomp_4_gpio))
  with open('settings.ini', 'w') as configfile:
    config.write(configfile)
  return gpio

def set_config_time(time):
  config = ConfigParser()
  config.read('settings.ini')
  config.set('time', 'time', str(time.time))
  with open('settings.ini', 'w') as configfile:
    config.write(configfile)
  return time

def set_config_mlpersec(mlpersec):
  config = ConfigParser()
  config.read('settings.ini')
  config.set('mlpersec', 'mlpersec', str(mlpersec.mlpersec))
  with open('settings.ini', 'w') as configfile:
    config.write(configfile)
  return mlpersec