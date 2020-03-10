# create a factory object
from pykml.factory import KML_ElementMaker as KML
name_object = KML.name("Hello World!")
from pykml.factory import ATOM_ElementMaker as ATOM
from pykml.factory import GX_ElementMaker as GX
pm1 = KML.Placemark(
		KML.name("Hello World!"),
		KML.Point(
			KML.coordinates("-64.5253,18.4607")
		)	
	)
from lxml import etree
etree.tostring(pm1)
print etree.tostring(pm1,pretty_print = True)
pm2 = KML.Placemark(
		KML.name("A Second Placemark!"),
		KML.Point(
			KML.coordinates("-64.5358, 18.4486")
			)
		)
fld = KML.Folder(pm1,pm2)
print etree.tostring(fld,pretty_print=True)
pm3 = KML.Placemark(KML.name("A THIRD placemark!"))
fld.append(pm3)
print etree.tostring(fld, pretty_print=True)
fld.remove(pm2)
print etree.tostring(fld, pretty_print=True)
print fld.Placemark.name.text
from pykml import parser
kml_str = '<kml xmlns="http://www.opengis.net/kml/2.2">' \
			'<Document>' \
				'<Folder>' \
					'<name>sample folder</name>' \
				'</Folder>' \
			'</Document>' \
		'</kml>'
root = parser.fromstring(kml_str)
print root.Document.Folder.name.text
from os import path
kml_file = path.join( \
    './test', \
    'Mouton_Citrus.kml')
with open(kml_file) as f:
	root = parser.parse(f).getroot()
print root.Document.name
