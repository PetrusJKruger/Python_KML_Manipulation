# create a factory object
from pykml.factory import KML_ElementMaker as KML
from pykml.factory import ATOM_ElementMaker as ATOM
from pykml.factory import GX_ElementMaker as GX
from lxml import etree
from pykml import parser
from os import path
from pykml.parser import Schema

#initialization
plcmNum = 3
fldNum = 1
fldName = []
myName = []
fldPlacemark = KML.Folder()
fldPolygon = KML.Folder()

kml_file = 'Mouton Citrus_Alles.kml'
with open(kml_file) as f:
	root = parser.parse(f).getroot()

cnt = len(root.Document.Folder.Folder)
print cnt