import xml.etree.ElementTree as ET
tree = ET.parse('filename.xml')
root = tree.getroot()

print root.tag

for child in root:
  print child.tag, child.attrib
  
for country in root.iter('country'):
    print country.attrib
#    for neighbor in child.iter():
#        print neighbor.attrib
