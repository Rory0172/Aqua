from configparser import ConfigParser
from flask import request

def get_volumes_client(self):
  self.pomp_1_volume = request.args.get('pomp1ml')
  self.pomp_2_volume = request.args.get('pomp2ml')
  self.pomp_3_volume = request.args.get('pomp3ml')
  self.pomp_4_volume = request.args.get('pomp4ml')
  return self

def get_schedules_client(self):
  #Get info from URL
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

def get_config(self):
  # parse existing file
  config = ConfigParser(allow_no_value=True)
  config.read('settings.ini')

  #Get info from existing config file
  self.pomp_1_volume = config.get('pomp', 'pomp1ml')
  self.pomp_2_volume = config.get('pomp', 'pomp2ml')
  self.pomp_3_volume = config.get('pomp', 'pomp3ml')
  self.pomp_4_volume = config.get('pomp', 'pomp4ml')
  return self

def set_config(volumes, schedules):
  config = ConfigParser()
  config.read('settings.ini')
  config.set('pomp', 'pomp1ml', str(volumes.pomp_1_volume))
  config.set('pomp', 'pomp2ml', str(volumes.pomp_2_volume))
  config.set('pomp', 'pomp3ml', str(volumes.pomp_3_volume))
  config.set('pomp', 'pomp4ml', str(volumes.pomp_4_volume))
  config.set('pomp', 'pomp1', str(schedules.schedule_pomp_1))
  config.set('pomp', 'pomp2', str(schedules.schedule_pomp_2))
  config.set('pomp', 'pomp3', str(schedules.schedule_pomp_3))
  config.set('pomp', 'pomp4', str(schedules.schedule_pomp_4))
  with open('settings.ini', 'w') as configfile:
    config.write(configfile)
  return volumes, schedules

def set_schedules_config(self):
  config.set('pomp', 'pomp1', str(pomp1clean))
  config.set('pomp', 'pomp2', str(pomp2clean))
  config.set('pomp', 'pomp3', str(pomp3clean))
  config.set('pomp', 'pomp4', str(pomp4clean))