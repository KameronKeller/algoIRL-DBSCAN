import math
from point import Point

# Input: DB: Database
# Input: ε: Radius
# Input: minPts: Density threshold
# Input: dist: Distance function
# Data: label: Point labels, initially undefined

x1 = Point([0,0])
x2 = Point([1,0])
x3 = Point([1,1])
x4 = Point([2,2])
x5 = Point([3,1])
x6 = Point([3,0])
x7 = Point([0,1])
x8 = Point([3,2])
x9 = Point([6,3])

data_set = [x1, x2, x3, x4, x5, x6, x7, x8, x9]

# for point in database:
# 	if point not labeled:
# 		# get neighbors
# 		neighbors = neighbors(data_set, point, radius)
# 	else:
# 		return
# 	if number(neighbors) < min_points:
# 		point.label = "noise"
# 		return
# 	c = "next cluster label"
# 	label(p) = c
# 	seed_set = (neighbors \ {p}) # seed set = set difference of neighbors and p
# 	for q in seed_set:
# 		if label(q) = "noise":
# 			label(q) = c
# 		elif label(q) != None:
# 			neighbors = range_query(database, min_distance, point, radius)
# 			label(q) = c
# 		if number(neighbors) < min_points:
# 			seed_set += neighbors


def neighbors(data_set, point, radius):
	neighbors = []
	for other_point in data_set:
		if math.dist(point.coords(), other_point.coords()) <= radius:
			neighbors.append(other_point)
	return neighbors

print(neighbors(data_set, x1, 1))


# 1. find neighbors

# 1.1 get neighbors as list
# 1.2 


# 2. create clusters with core points


# 3. assign border and noise points

