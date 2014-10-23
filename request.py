import urllib, time, datetime
import xml.dom.minidom
import xml.etree.ElementTree as ET

#timetable information
ttdurl = "/cgi-bin/rtpi/timetableinformation?"
host = "www.dublinked.ie"
header = "http://linqi:1710qi2014@"
ttdquery = urllib.urlencode({'type': 'day', 'stopid': '262', 'operator': 'bac', 'format': 'xml'})

#realtime bus information
rturl = "/cgi-bin/rtpi/realtimebusinformation?"
host = "www.dublinked.ie"
header = "http://linqi:1710qi2014@"
rtquery = urllib.urlencode({'stopid': '184', 'routeid': '4', 'operator': 'bac', 'format': 'xml'})

#request url
request = header + host + rturl + rtquery

#beginning timestamp
ts1 = time.time()
st1 = datetime.datetime.fromtimestamp(ts1).strftime('%Y-%m-%d %H:%M:%S')
print "\nSTART TIMESTAMP"
print st1

#get file from request
f = urllib.urlopen(request)
g = str(f.read())

#input xml to output.xml
input_xml = open("output.xml", "w")
input_xml.write("""<?xml version="1.0" encoding="ISO-8859-1" ?>""") #This line does the trick!
input_xml.write(g)
input_xml.close()

#open xml file and parse it
tree = ET.parse("output.xml")
root = tree.getroot()

#Have fun here:)
for child in root:
	print child.tag, child.attrib

print "\n===============================\n"

print root[5]

for i in root[5]:
	print i[1].text

f.close()

#end timestamp
ts2 = time.time()
st2 = datetime.datetime.fromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')
print "\nEND TIMESTAMP"
print st2

