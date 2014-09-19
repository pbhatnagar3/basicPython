# this program adds up integers in the command line
import sys
try:
	total = sum(int(arg) for arg in sys.argv[1:])
	print 'total value : %0.2f' %total
except ValueError:
	print 'Please supply integer arguments'
