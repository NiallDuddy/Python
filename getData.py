import rtpi
import time, datetime
import xml.dom.minidom
import xml.etree.ElementTree as ET
import json

#define variables
table = 'r' # t for timetable information, r for realtime bus information
stop = '262'
route = '16'
fo = 'json' # xml/json

#beginning timestamp
ts1 = time.time()
st1 = datetime.datetime.fromtimestamp(ts1).strftime('%Y-%m-%d %H:%M:%S')
print "\nBEFORE " + st1

rtpi.req(table, stop, route, fo)

if fo == 'xml':
	#open xml file and parse it
	tree = ET.parse("output_"+stop+".xml")
	root = tree.getroot()

	#Have fun here:)
	for child in root:
		print child.tag, child.attrib

	print "\n===============================\n"

	print root[5]

	for i in root[5]:
		print i[1].text

elif fo == 'json':
	#json_data = open("output_"+stop+".json")
	json_data = open("sample.json")
	data = json.load(json_data)
	json_data.close()

	print "stopid: " + data["stopid"]
	print "------------------------------"
	for i in data["results"]:
		print "route: " + i["route"]
		print "duetime: " + i["duetime"]
		print "destination: " + i["destination"]
		print "------------------------------"


#end timestamp
ts2 = time.time()
st2 = datetime.datetime.fromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')
print "AFTER " + st2
