def computeNearestNeighbor(username, users):
	"""creates a sorted list of users based on their distance to
	username"""
	distances = []
	for user in users:
		if user != username:
			distance = manhattan(users[user], users[username])
			distances.append((distance, user))
	# sort based on distance -- closest first
	distances.sort()
	return distances
