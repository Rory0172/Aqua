from configparser import ConfigParser
from flask import request

def get_volumes_client(self):
  self.pump_1_volume = request.args.get('pump1ml')
  self.pump_2_volume = request.args.get('pump2ml')
  self.pump_3_volume = request.args.get('pump3ml')
  self.pump_4_volume = request.args.get('pump4ml')
  return self

def get_schedules_client(self):
  pump1maandag = request.args.get('pump1maandag')
  pump1dinsdag = request.args.get('pump1dinsdag')
  pump1woensdag = request.args.get('pump1woensdag')
  pump1donderdag = request.args.get('pump1donderdag')
  pump1vrijdag = request.args.get('pump1vrijdag')
  pump1zaterdag = request.args.get('pump1zaterdag')
  pump1zondag= request.args.get('pump1zondag')

  pump2maandag = request.args.get('pump2maandag')
  pump2dinsdag = request.args.get('pump2dinsdag')
  pump2woensdag = request.args.get('pump2woensdag')
  pump2donderdag = request.args.get('pump2donderdag')
  pump2vrijdag = request.args.get('pump2vrijdag')
  pump2zaterdag = request.args.get('pump2zaterdag')
  pump2zondag= request.args.get('pump2zondag')

  pump3maandag = request.args.get('pump3maandag')
  pump3dinsdag = request.args.get('pump3dinsdag')
  pump3woensdag = request.args.get('pump3woensdag')
  pump3donderdag = request.args.get('pump3donderdag')
  pump3vrijdag = request.args.get('pump3vrijdag')
  pump3zaterdag = request.args.get('pump3zaterdag')
  pump3zondag= request.args.get('pump3zondag')

  pump4maandag = request.args.get('pump4maandag')
  pump4dinsdag = request.args.get('pump4dinsdag')
  pump4woensdag = request.args.get('pump4woensdag')
  pump4donderdag = request.args.get('pump4donderdag')
  pump4vrijdag = request.args.get('pump4vrijdag')
  pump4zaterdag = request.args.get('pump4zaterdag')
  pump4zondag= request.args.get('pump4zondag')

  self.schedule_pump_1 = (str(pump1maandag) + str(pump1dinsdag) + str(pump1woensdag) + str(pump1donderdag) + str(pump1vrijdag) + str(pump1zaterdag) + str(pump1zondag)).replace("None", '')
  self.schedule_pump_2 = (str(pump2maandag) + str(pump2dinsdag) + str(pump2woensdag) + str(pump2donderdag) + str(pump2vrijdag) + str(pump2zaterdag) + str(pump2zondag)).replace("None", '')
  self.schedule_pump_3 = (str(pump3maandag) + str(pump3dinsdag) + str(pump3woensdag) + str(pump3donderdag) + str(pump3vrijdag) + str(pump3zaterdag) + str(pump3zondag)).replace('None', '')
  self.schedule_pump_4 = (str(pump4maandag) + str(pump4dinsdag) + str(pump4woensdag) + str(pump4donderdag) + str(pump4vrijdag) + str(pump4zaterdag) + str(pump4zondag)).replace('None', '')
  return self

def get_volume_reservoirs_client(self):
  self.pump_1_volume_reservoir = request.args.get('reservoir1')
  self.pump_2_volume_reservoir = request.args.get('reservoir2')
  self.pump_3_volume_reservoir = request.args.get('reservoir3')
  self.pump_4_volume_reservoir = request.args.get('reservoir4')
  return self

def get_alias_client(self):
  self.alias_1 = request.args.get('alias_1')
  self.alias_2 = request.args.get('alias_2')
  self.alias_3 = request.args.get('alias_3')
  self.alias_4 = request.args.get('alias_4')
  return self

def get_gpio_client(self):
  self.pump_1_gpio = request.args.get('pump1gpio')
  self.pump_2_gpio = request.args.get('pump2gpio')
  self.pump_3_gpio = request.args.get('pump3gpio')
  self.pump_4_gpio = request.args.get('pump4gpio')
  return self

def get_time_client(self):
  self.time = request.args.get('time')
  return self

def get_mlpersec_client(self):
  self.mlpersec = request.args.get('mlpersec')
  return self

def get_volume_available_ml_client(self):
  if request.args.get('vol_res_1'): self.volume_available_1_ml = request.args.get('vol_res_1') 
  if request.args.get('vol_res_2'): self.volume_available_2_ml = request.args.get('vol_res_2') 
  if request.args.get('vol_res_3'): self.volume_available_3_ml = request.args.get('vol_res_3') 
  if request.args.get('vol_res_4'): self.volume_available_4_ml = request.args.get('vol_res_4') 
  return self

def get_config_volume(self):
  config = ConfigParser(allow_no_value=True)
  config.read('settings.ini')
  self.pump_1_volume = config.get('pump', 'pump_1_volume')
  self.pump_2_volume = config.get('pump', 'pump_2_volume')
  self.pump_3_volume = config.get('pump', 'pump_3_volume')
  self.pump_4_volume = config.get('pump', 'pump_4_volume')
  return self 

def get_config_volume_available(self):
  config = ConfigParser(allow_no_value=False)
  config.read('settings.ini')
  self.volume_available_1 = config.get('volume_available', 'volume_available_1')
  self.volume_available_2 = config.get('volume_available', 'volume_available_2')
  self.volume_available_3 = config.get('volume_available', 'volume_available_3')
  self.volume_available_4 = config.get('volume_available', 'volume_available_4')  
  return self 

def get_config_alias(self):
  config = ConfigParser(allow_no_value=False)
  config.read('settings.ini')
  self.alias_1 = config.get('alias', 'alias_1')
  self.alias_2 = config.get('alias', 'alias_2')
  self.alias_3 = config.get('alias', 'alias_3')
  self.alias_4 = config.get('alias', 'alias_4')  
  return self 

def get_config_schedules(self):
  config = ConfigParser(allow_no_value=True)
  config.read('settings.ini')
  self.schedule_pump_1 = config.get('pump', 'schedule_pump_1')
  self.schedule_pump_2 = config.get('pump', 'schedule_pump_2')
  self.schedule_pump_3 = config.get('pump', 'schedule_pump_3')
  self.schedule_pump_4 = config.get('pump', 'schedule_pump_4')
  return self 

def get_config_volume_reservoirs(self):
  config = ConfigParser(allow_no_value=True)
  config.read('settings.ini')
  self.pump_1_volume_reservoir = config.get('reservoir', 'reservoir1')
  self.pump_2_volume_reservoir = config.get('reservoir', 'reservoir2')
  self.pump_3_volume_reservoir = config.get('reservoir', 'reservoir3')
  self.pump_4_volume_reservoir = config.get('reservoir', 'reservoir4')
  return self

def get_config_gpio(self):
  config = ConfigParser(allow_no_value=True)
  config.read('settings.ini')
  self.pump_1_gpio = config.get('gpio', 'pump_1_gpio')
  self.pump_2_gpio = config.get('gpio', 'pump_2_gpio')
  self.pump_3_gpio = config.get('gpio', 'pump_3_gpio')
  self.pump_4_gpio = config.get('gpio', 'pump_4_gpio')
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
  config.set('pump', 'pump_1_volume', str(volumes.pump_1_volume))
  config.set('pump', 'pump_2_volume', str(volumes.pump_2_volume))
  config.set('pump', 'pump_3_volume', str(volumes.pump_3_volume))
  config.set('pump', 'pump_4_volume', str(volumes.pump_4_volume))
  config.set('pump', 'schedule_pump_1', str(schedules.schedule_pump_1))
  config.set('pump', 'schedule_pump_2', str(schedules.schedule_pump_2))
  config.set('pump', 'schedule_pump_3', str(schedules.schedule_pump_3))
  config.set('pump', 'schedule_pump_4', str(schedules.schedule_pump_4))
  with open('settings.ini', 'w') as configfile:
    config.write(configfile)
  return volumes, schedules

def set_config_volume_reservoirs(volume_reservoirs):
  config = ConfigParser()
  config.read('settings.ini')
  config.set('reservoir', 'reservoir1', str(volume_reservoirs.pump_1_volume_reservoir))
  config.set('reservoir', 'reservoir2', str(volume_reservoirs.pump_2_volume_reservoir))
  config.set('reservoir', 'reservoir3', str(volume_reservoirs.pump_3_volume_reservoir))
  config.set('reservoir', 'reservoir4', str(volume_reservoirs.pump_4_volume_reservoir))
  with open('settings.ini', 'w') as configfile:
    config.write(configfile)
  return volume_reservoirs

def set_config_alias(alias):
  config = ConfigParser()
  config.read('settings.ini')
  config.set('alias', 'alias_1', str(alias.alias_1))
  config.set('alias', 'alias_2', str(alias.alias_2))
  config.set('alias', 'alias_3', str(alias.alias_3))
  config.set('alias', 'alias_4', str(alias.alias_4))
  with open('settings.ini', 'w') as configfile:
    config.write(configfile)
  return alias

def set_config_gpio(gpio):
  config = ConfigParser()
  config.read('settings.ini')
  config.set('gpio', 'pump_1_gpio', str(gpio.pump_1_gpio))
  config.set('gpio', 'pump_2_gpio', str(gpio.pump_2_gpio))
  config.set('gpio', 'pump_3_gpio', str(gpio.pump_3_gpio))
  config.set('gpio', 'pump_4_gpio', str(gpio.pump_4_gpio))
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

def set_config_volume_available_ml(volume_available_ml, volume_reservoirs):
  config = ConfigParser()
  config.read('settings.ini') 

  pump_numbers = [0,1,2,3]

  for pump_number in pump_numbers:
    if pump_number == 0:
      volume_available = int(100 * int(volume_available_ml.volume_available_1_ml) / int(volume_reservoirs.pump_1_volume_reservoir))
      config.set('volume_available', 'volume_available_1_ml', str(volume_available_ml.volume_available_1_ml))
      config.set('volume_available', 'volume_available_1', str(volume_available))

    elif pump_number == 1:
      volume_available = int(100 * int(volume_available_ml.volume_available_2_ml) / int(volume_reservoirs.pump_2_volume_reservoir))
      config.set('volume_available', 'volume_available_2_ml', str(volume_available_ml.volume_available_2_ml))
      config.set('volume_available', 'volume_available_2', str(volume_available))

    elif pump_number == 2:
      volume_available = int(100 * int(volume_available_ml.volume_available_3_ml) / int(volume_reservoirs.pump_3_volume_reservoir))
      config.set('volume_available', 'volume_available_3_ml', str(volume_available_ml.volume_available_3_ml))
      config.set('volume_available', 'volume_available_3', str(volume_available))

    elif pump_number == 3:
      volume_available = int(100 * int(volume_available_ml.volume_available_4_ml) / int(volume_reservoirs.pump_4_volume_reservoir))
      config.set('volume_available', 'volume_available_4_ml', str(volume_available_ml.volume_available_4_ml))
      config.set('volume_available', 'volume_available_4', str(volume_available))

  with open('settings.ini', 'w') as configfile:
    config.write(configfile)
  return volume_available_ml

