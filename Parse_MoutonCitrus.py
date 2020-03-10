# create a factory object
from pykml.factory import KML_ElementMaker as KML
from pykml.factory import ATOM_ElementMaker as ATOM
from pykml.factory import GX_ElementMaker as GX
from lxml import etree
from pykml import parser
from os import path
from pykml.parser import Schema

#initialization
plcmNum = 4
fldNum = 1
fldName = []
myName = []
fldPlacemark = KML.Folder()
fldPolygon = KML.Folder()

kml_file = path.join( \
    './test', \
    'Mouton_Citrus.kml')
with open(kml_file) as f:
	root = parser.parse(f).getroot()

for i in range(0,fldNum):
	fldName.append('MC - ' + root.Document.Folder.Folder[i].name.text)
	print fldName[i]
	for j in range(0,plcmNum):
		if j & 1:
			myName.append(myName[j-1])
			pm1 = KML.Placemark(
				KML.name(myName[j]),
				KML.Polygon(
					KML.tessellate(1),
					KML.outerBoundaryIs(
						KML.LinearRing(root.Document.Folder.Folder[i].Placemark[j].Polygon.outerBoundaryIs.LinearRing.coordinates)
						)
					)
				)
			fldPolygon.append(pm1)
		else:
			myName.append(fldName[i] + ' - ' + root.Document.Folder.Folder.Placemark[j].name.text)
			pm2 = KML.Placemark(
				KML.name(myName[j]),
				KML.Point(root.Document.Folder.Folder[i].Placemark[j].Point.coordinates
					)
				)
			fldPlacemark.append(pm2)

#for i in range(0,plcmNum):
#		print myName[i]


#print '------------'
#cor = root.Document.Folder.Folder[0].Placemark[2].Polygon.outerBoundaryIs.LinearRing.coordinates
#print cor

print '------------'
print etree.tostring(fldPlacemark, pretty_print = True)

# output a KML file (named based on the Python script)
#outfile = file(__file__.rstrip('.py')+'.kml','w')
#outfile.write(etree.tostring(fldPolygon, pretty_print=True))

#assert Schema('kml22gx.xsd').assertValid(fldPolygon)

# output a KML file (named based on the Python script)
outfile = file(__file__.rstrip('.py')+'.kml','w')
outfile.write(etree.tostring(fldPlacemark, pretty_print=True))

#assert Schema("ogckml22.xsd").validate(fldPlacemark)