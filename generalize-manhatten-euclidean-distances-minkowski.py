def minkowski(rating1, rating2, r):
	"""Computes the Minkowski distance.
	Both rating1 and rating2 are dictionaries of the form
	{'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""

	distance = 0
	commonRatings = False
	for key in rating1:
		if key in rating2:
			distance +=	pow(abs(rating1[key] - rating2[key]), r)
		commonRatings = True
	if commonRatings:
		return pow(distance, 1/r)
	else:
		return 0 #Indicates no ratings in common