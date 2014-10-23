import xml.dom.minidom

f = open("sample.xml","r")
g = str(f.read())
xml = xml.dom.minidom.parseString(g)
pretty_xml_as_string = xml.toprettyxml()

print pretty_xml_as_string

f.close()