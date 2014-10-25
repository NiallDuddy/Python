import rtpi
import time, datetime
import xml.dom.minidom
import xml.etree.ElementTree as ET
import json


#define variables
## will convert these variables to user inputs later ##
table = 'r' # t for timetable information, r for realtime bus information
stop = '262'
route = '16'
fo = 'json' # format = xml/json?

#beginning timestamp
ts1 = time.time()
st1 = datetime.datetime.fromtimestamp(ts1).strftime('%Y-%m-%d %H:%M:%S')
print "\nBEFORE " + st1

#retrieve rtpi data
rtpi.req(table, stop, route, fo)

#if format == "xml"
if fo == 'xml':

	#xml file
	xml_output = "output_"+stop+".xml"

	#print xml file to console
	xml_data = xml.dom.minidom.parse(xml_output)
	pretty_xml_as_string = xml_data.toprettyxml()
	print pretty_xml_as_string
	print "---------------------------------------"

	#parse xml file
	print "OPEN FILE: " + xml_output
	tree = ET.parse(xml_output)
	root = tree.getroot()

	for child in root:
		print child.tag, child.attrib

	print "\n---------------------------------------\n"

	print root[5]

	for i in root[5]:
		print i[1].text

#if format == "json"
elif fo == 'json':
	
	#json file
	json_output = "output_"+stop+".json"

	#open json file
	print "OPEN FILE: " + json_output
	json_data = open(json_output)
	data = json.load(json_data)
	json_data.close()

	#print json file to console
	print json.dumps(data, indent=4)

	#parse json file
	print ""
	print "stopid: " 							+ data["stopid"]
	print "---------------------------------------"
	for i in data["results"]:
		print "arrivaldatetime: " 				+ i["arrivaldatetime"]
		print "duetime: " 						+ i["duetime"]
		print "departuredatetime: " 			+ i["departuredatetime"] 
		print "departureduetime: "				+ i["departureduetime"]
		print "scheduledarrivaldatetime: " 		+ i["scheduledarrivaldatetime"]
		print "scheduleddeparturedatetime: "  	+ i["scheduleddeparturedatetime"]
		print "destination: " 					+ i["destination"]
		print "destinationlocalized: "			+ i["destinationlocalized"]
		print "origin: "						+ i["origin"]
		print "originlocalized: "				+ i["originlocalized"]
		print "direction: "						+ i["direction"]
		print "operator: "						+ i["operator"]
		print "additionalinformation: "			+ i["additionalinformation"]
		print "lowfloorstatus: "				+ i["lowfloorstatus"]
		print "route: " 						+ i["route"]
		print "sourcetimestamp: "				+ i["sourcetimestamp"]
		print "---------------------------------------"


#end timestamp
ts2 = time.time()
st2 = datetime.datetime.fromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')
print "AFTER " + st2
