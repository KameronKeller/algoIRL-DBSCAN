# Input: DB: Database
# Input: ε: Radius
# Input: minPts: Density threshold
# Input: dist: Distance function
# Data: label: Point labels, initially undefined



for point in database:
	if label(p) == None:
		neighbors = range_query(database, min_distance, point, radius)
	if number(neighbors) < min_points:
		p.label = "noise"
	c = "next cluster label"
	label(p) = c
	seed_set = (neighbors \ {p}) # seed set = set difference of neighbors and p
	for q in seed_set:
		if label(q) = "noise":
			label(q) = c
		elif label(q) != None:
			neighbors = range_query(database, min_distance, point, radius)
			label(q) = c
		if number(neighbors) < min_points:
			seed_set += neighbors










