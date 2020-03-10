# create a factory object
from pykml.factory import KML_ElementMaker as KML
from pykml.factory import ATOM_ElementMaker as ATOM
from pykml.factory import GX_ElementMaker as GX
from lxml import etree
from pykml import parser
from os import path
from pykml.parser import Schema

#initialization

fldName = []
myName = []
fldPlacemark = KML.Folder()
fldPolygon = KML.Folder()

kml_file = 'Mouton Citrus_Alles.kml'
with open(kml_file) as f:
	root = parser.parse(f).getroot()

fldNum = len(root.Document.Folder.Folder)


for i in range(0,fldNum):
	fldName.append('MC - ' + root.Document.Folder.Folder[i].name.text)
	print fldName[i]
	plcmNum = len(root.Document.Folder.Folder[i].Placemark)
	print plcmNum
	del myName
	myName = []
	for j in range(0,plcmNum):
		tmp1 = root.Document.Folder.Folder[i].Placemark[j].name.text
		tmp2 = unicode(tmp1[:1], "utf-8")
		if not tmp2.isnumeric():
			myName.append(fldName[i] + ' - ' + root.Document.Folder.Folder[i].Placemark[j].name.text)
			#print 'Blok  --> ' + myName[j]
			pm2 = KML.Placemark(
				KML.name(myName[j]),
				KML.Point(root.Document.Folder.Folder[i].Placemark[j].Point.coordinates
					)
				)
			fldPlacemark.append(pm2)
		else:
			print myName[j-1]
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

#for i in range(0,plcmNum):
#		print myName[i]


#print '------------'
#cor = root.Document.Folder.Folder[0].Placemark[2].Polygon.outerBoundaryIs.LinearRing.coordinates
#print cor

print '------------'
#print etree.tostring(fldPlacemark, pretty_print = True)

print '------------'
#print etree.tostring(fldPolygon, pretty_print = True)

# output a KML file (named based on the Python script)
outfile = file('AGNAV_MC Polygons.kml','w')
outfile.write(etree.tostring(fldPolygon, pretty_print=True))

#assert Schema('kml22gx.xsd').assertValid(fldPolygon)

# output a KML file (named based on the Python script)
outfile = file('AGNAV_MC Placemarks.kml','w')
outfile.write(etree.tostring(fldPlacemark, pretty_print=True))

#assert Schema("ogckml22.xsd").validate(fldPlacemark)