import ConfigParser
import console
 
file_name = 'build_def.txt'
print 'Reading config file %s.' % file_name
Config = ConfigParser.ConfigParser()
Config.read(file_name)
print('%i sections' %
(len(Config.sections())))
for section in Config.sections():
print(' %s' % section)
items = Config.items(section)
print(' %s' % items)
