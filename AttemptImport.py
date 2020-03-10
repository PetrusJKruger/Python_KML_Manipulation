from pykml.factory import KML_ElementMaker as KML
from pykml.factory import ATOM_ElementMaker as ATOM
from pykml.factory import GX_ElementMaker as GX
from lxml import etree
from pykml import parser

from pykml.factory import write_python_script_for_kml_document
from os import path
kml_file = path.join( \
    './test', \
    'Mouton_Citrus.kml')
with open(kml_file) as f:
	doc = parser.parse(f).getroot()

script = write_python_script_for_kml_document(doc)

print script
print etree.tostring(etree.ElementTree(doc),pretty_print=True)