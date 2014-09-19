from time import localtime

activities = {
	8: 'Sleeping',
	9: 'Commuting',
	12: 'working',
	0: 'will continue to sleep'
}

time_now = localtime()
# hour = time_now.tm_hour
hour = 48

for activity_time in sorted(activities.keys()):
	if hour < activity_time:
		print activities[activity_time]
		break
else:
	print 'Unknown, AFK or playing'
