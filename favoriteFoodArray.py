# making an array and iterating through iterating
favoriteFood = ['Orange', 'Papaya', 'Watermelon']
for currentFood in favoriteFood:
	print 'you can have ' + currentFood

#there is another way we can do this
for i, currentFood in enumerate(favoriteFood):
	print '{iteration} will be eating the {cf}'.format(iteration = i, cf = currentFood)
