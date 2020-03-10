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
#print etree.tostring(pm1,pretty_print = True)
pm2 = KML.Placemark(
		KML.name("A Second Placemark!"),
		KML.Point(
			KML.coordinates("-64.5358, 18.4486")
			)
		)
fld = KML.Folder(pm1,pm2)
#print etree.tostring(fld,pretty_print=True)

print pm1.name.text

pm1.name = "Hi World!"

print etree.tostring(fld, pretty_print=True)