import math
from random import seed
from point import Point

# Input: DB: Database
# Input: ε: Radius
# Input: minPts: Density threshold
# Input: dist: Distance function
# Data: label: Point labels, initially undefined

x1 = Point([0,0])
x2 = Point([1,0])
x3 = Point([1,1])
# x4 = Point([2,2])
# x5 = Point([3,1])
# x6 = Point([3,0])
x7 = Point([0,1])
# x8 = Point([3,2])
x9 = Point([6,3])

# data_set = [x1, x2, x3, x4, x5, x6, x7, x8, x9]
data_set = [x1, x2, x3, x7]

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


def range_query(data_set, point, radius):
	neighbors = []
	for other_point in data_set:
		print("          dist from", point, "to", other_point, "is", math.dist(point.coords(), other_point.coords()))
		if math.dist(point.coords(), other_point.coords()) <= radius:
			neighbors.append(other_point)
	return neighbors

# print(range_query(data_set, x1, 1))

def dbscan(data, neighbor_range, density_threshold):
	print("Data:", data)
	cluster_id = 0
	for point in data:
		print(cluster_id, "------------------------------------------")
		print("point", point, "label:", point.label)
		if point.label is not None:
			print("go to next point if label is not None")
			continue
		set_of_neighbors = range_query(data, point, neighbor_range)
		print("neighbors:", set_of_neighbors)
		if len(set_of_neighbors) < density_threshold:
			point.set_label("Noise")
			print("go to next point if len(set_of_neighbors) < density_threshold")
			continue
		cluster_label = f'cluster_{cluster_id}'
		point.set_label(cluster_label)
		set_of_neighbors.remove(point)
		seed_set = set_of_neighbors
		print("seed_set:", seed_set)
		for neighbor in seed_set:
			print("     --------------------------------------")
			print("     ", "neighbor:", neighbor, "label:", neighbor.label)
			if neighbor.label == "Noise":
				neighbor.label = cluster_label
				print("     ", "label", neighbor, "cluster_label")
			if neighbor.label is not None:
				print("     ", "go to next neighbor if label is not None")
				continue
			next_set_of_neighbors = range_query(data, point, neighbor_range)
			print("     ", "next_set_of_neighbors:", next_set_of_neighbors)
			neighbor.label = cluster_label
			print("     ", "neighbor:", neighbor, "label:", neighbor.label)
			if len(next_set_of_neighbors) < density_threshold:
				print("     ", "go to next neighbor if len(set_of_neighbors) < density_threshold")
				continue
			seed_set = seed_set + next_set_of_neighbors
			print("     ", "seed_set for next inner loop:", seed_set)
			for neighbor in seed_set:
					print("          ", "neighbor:", neighbor, neighbor.label)
			print("     -------------END----------------------\n")
		print("-------------------END----------------------\n\n")
		cluster_id += 1

dbscan(data_set, 1, 3)
num = 1
for point in data_set:
	print("point ", num, "label:", point.label, "coords: ", point.coords())
	num += 1
