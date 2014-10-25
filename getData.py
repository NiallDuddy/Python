import time, datetime
import rtpi

# examle inputs:
# table = 'r' # r for realtime bus information, t for timetable information
# stop = '262'
# route = '16' #optional
# fo = 'j' # format = xml/json?

# This UI is designed for testing 
while True:

	# Get table type
	print "What Dublinbus information you want to retrieve? "
	table = raw_input("""USAGE:\n'r' for realtime bus information\n't' for timetable informationn\n'q' to quit: """)
	# Check if quit
	if table in ('q', 'Q'):
		print 'QUIT'
		exit()
	# Check if realtime info or timetable info
	if table not in ('r', 't', 'R', 'T'):
		print """Please enter in 'r', 't' or 'q'."""
		continue	
	
	# Get bus stop no.
	stop = raw_input('''What bus stop no. you're looking for: ''')
	# Check if a number
	try:
		stop = int(stop)
	except ValueError:
		print('Please enter in a number.\n')
		continue 
	
	# Get bus route no.
	route = raw_input('''What bus route you're looking for: ''')
	# Check if a number
	try:
		route = int(route)
	except ValueError:
		print('Please enter in a number.\n')
		continue 
	
	# Get bus route no.
	fo = raw_input('''What format(xml/json) do you want: ''')
	# Check inputs
	if fo == 'x': fo = 'xml'
	if fo == 'j': fo = 'json'
	# Check if valid
	if fo not in ('xml', 'json', 'x', 'j'):
		print """Please enter in 'xml', 'x' or 'json', 'j'."""
		continue
	
	# Print results
	print('BEFORE: %s' % time.ctime())
	rtpi.ppdata(table, str(stop), str(route), fo)
	print('AFTER: %s\n' % time.ctime())

