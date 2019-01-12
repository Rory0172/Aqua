from configparser import ConfigParser

# instantiate
config = ConfigParser()

# parse existing file
config.read('next.ini')

# read values from a section
mlpersec = config.get('mlpersec', 'mlpersec')
bool_val = config.getboolean('pomp', 'bool_val')
int_val = config.getint('pomp', 'int_val')
#float_val = config.getfloat('section_a', 'pi_val')
print (int_val)
# update existing value
config.set('section_a', 'string_val', str(bool_val))

# add a new section and some values
#config.add_section('section_b')
#config.set('section_b', 'meal_val', 'spam')
#config.set('section_b', 'not_found_val', 404)

# save to a file
with open('test.ini', 'w') as configfile:
	config.write(configfile)
