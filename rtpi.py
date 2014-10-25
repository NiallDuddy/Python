# -*- coding: utf-8 -*-
import urllib, time, datetime
import xml.dom.minidom
import json


def req(table, stop, route, fo):

	#default request
	request = """http://linqi:1710qi2014@
	www.dublinked.ie
	/cgi-bin/rtpi/
	realtimebusinformation?stopid=1&operator=bac
	"""

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
	g = f.read()
	f.close()

	if fo == "xml":

		#input xml to output_stopid.xml
		input_xml = open("output_"+stop+".xml", "w")
		input_xml.write("""<?xml version="1.0" encoding="ISO-8859-1" ?>""") #This line does the trick!
		input_xml.write(g)
		input_xml.close()

	elif fo == "json":

		#input xml to output_stopid.json
		input_json = open("output_"+stop+".json", 'w')
		input_json.write(g)
		input_json.close()


