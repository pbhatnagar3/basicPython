#indent your python code to pit into an email
import glob
# glob supports Unix styles pathname extensions
python_files = glob.glob('*.py')
for current_file in sorted(python_files):
	print '		------' + current_file

	with open(current_file) as f:
		for line in f:
			print '				' + line.rstrip()		
	print
