import xml.etree.ElementTree as ET
tree = ET.parse('xml.xml')
root = tree.getroot()

root.tag

for myYear in root.iter('year'):
	myName = myYear.text
	print myName
#for country in root.findall('country'):
#	gp = country.find('gdppc').text
#	print gp

