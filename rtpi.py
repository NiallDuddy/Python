# -*- coding: utf-8 -*-
import urllib, time, datetime
import xml.dom.minidom
import xml.etree.ElementTree as ET
import json


def ppdata(table, stop, route, fo):
	"""Parse and print data from local files(xml/json)."""

	#retrieve rtpi data to local files
	req(table, stop, route, fo)

	#if format == "xml"
	if fo == 'xml':

		#xml file
		xml_output = "output_"+stop+".xml"

		#print xml file to console
		print "OPEN FILE: " + xml_output
		xml_data = xml.dom.minidom.parse(xml_output)
		pretty_xml_as_string = xml_data.toprettyxml()
		print pretty_xml_as_string
		print "---------------------------------------"

		#parse xml file
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



def req(table, stop, route, fo):
	"""Retrieve rtpi data(xml/json) to local files."""

	#Replace user and password with API key
	#default request
	request = """http://[user]:[password]@
	www.dublinked.ie
	/cgi-bin/rtpi/
	realtimebusinformation?stopid=1&operator=bac
	"""

	if table == "t":

		#timetable information
		tturl = "/cgi-bin/rtpi/timetableinformation?"
		host = "www.dublinked.ie"
		header = "http://[user]:[password]@"
		ttquery = urllib.urlencode({'type': 'day', 'stopid': stop, 'operator': 'bac', 'format': fo})
		#request url
		request = header + host + tturl + ttquery

	elif table == "r":

		#realtime bus information
		rturl = "/cgi-bin/rtpi/realtimebusinformation?"
		host = "www.dublinked.ie"
		header = "http://[user]:[password]@"
		rtquery = urllib.urlencode({'stopid': stop, 'routeid': route, 'operator': 'bac', 'format': fo})
		#request url
		request = header + host + rturl + rtquery


	#get file from request
	f = urllib.urlopen(request)
	g = f.read()
	f.close()

	if fo == "xml":

		#save to output_stopid.xml
		input_xml = open("output_"+stop+".xml", "w")
		input_xml.write("""<?xml version="1.0" encoding="ISO-8859-1" ?>""") #This line does the trick!
		input_xml.write(g)
		input_xml.close()

	elif fo == "json":

		#save to output_stopid.json
		input_json = open("output_"+stop+".json", 'w')
		input_json.write(g)
		input_json.close()
