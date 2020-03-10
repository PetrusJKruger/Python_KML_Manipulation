from lxml import etree
from lxml import objectify

root = objectify.Element("root")
b = objectify.SubElement(root, "b")

x1 = objectify.SubElement(root, "x")
x2 = objectify.SubElement(root, "x")
x3 = objectify.SubElement(root, "x")

[ el.tag for el in root.x[1:3] ]
print el.v