# -*- coding: utf-8 -*-
import urllib, time, datetime
import xml.dom.minidom
import xml.etree.ElementTree as ET

table = 't' # t for timetable information, r for realtime bus information
stop = '184'
route = '4'
fo = 'xml' # xml/json

def req(table, stop, route, fo):

	#default request
	request = "http://linqi:1710qi2014@"
	+"www.dublinked.ie"
	+"/cgi-bin/rtpi/realtimebusinformation?"
	+"stopid=1&operator=bac"

	if table == "t":
		#timetable information
		tturl = "/cgi-bin/rtpi/timetableinformation?"
		host = "www.dublinked.ie"
		header = "http://linqi:1710qi2014@"
		ttquery = urllib.urlencode({'type': 'day', 'stopid': stop, 'operator': 'bac', 'format': fo})
		#request url
		request = header + host + tturl + ttquery
	elif table == "r":
		#realtime bus information
		rturl = "/cgi-bin/rtpi/realtimebusinformation?"
		host = "www.dublinked.ie"
		header = "http://linqi:1710qi2014@"
		rtquery = urllib.urlencode({'stopid': stop, 'routeid': route, 'operator': 'bac', 'format': fo})
		#request url
		request = header + host + rturl + rtquery


	#get file from request
	f = urllib.urlopen(request)
	g = str(f.read())
	print g

	if fo == "xml":
		#input xml to output.xml
		input_xml = open("output_"+stop+".xml", "w")
		input_xml.write("""<?xml version="1.0" encoding="ISO-8859-1" ?>""") #This line does the trick!
		input_xml.write(g)
		input_xml.close()
	elif fo == "json":
		input_json = open("output_"+stop+".json", 'w')
		input_json.write(g)
		input_json.close()




#beginning timestamp
ts1 = time.time()
st1 = datetime.datetime.fromtimestamp(ts1).strftime('%Y-%m-%d %H:%M:%S')
print "\nBEFORE"
print st1


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
print "\nAFTER"
print st2

