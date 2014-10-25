import urllib, xml.etree.ElementTree

ttdurl = "/cgi-bin/rtpi/timetableinformation?"
host = "www.dublinked.ie"
header = "http://[Username]:[Password]@"
ttdquery = urllib.urlencode({'type': 'day', 'stopid': '184', 'routeid': '4', 'operator': 'bac', 'format': 'xml'})

#rturl = "/cgi-bin/rtpi/realtimebusinformation?"
#host = "www.dublinked.ie"
#header = "http://linqi:1710qi2014@"
#rtquery = urllib.urlencode({'stopid': '184', 'routeid': '4', 'operator': 'bac', 'format': 'xml'})

request = header + host + ttdurl + ttdquery

response = urllib.urlopen(request).read()
decode = response.decode("windows-1252").encode("utf8")
root = xml.etree.ElementTree.fromstring(decode)

for result in root[5]:
    data = ""
    for value in result:
        data =  data + " " + value.text
    print data
