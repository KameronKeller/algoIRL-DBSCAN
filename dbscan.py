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
x4 = Point([2,2])
x5 = Point([3,1])
x6 = Point([3,0])
x7 = Point([0,1])
x8 = Point([3,2])
x9 = Point([6,3])

data_set = [x1, x2, x3, x4, x5, x6, x7, x8, x9]


def range_query(data_set, point, radius):
	neighbors = []
	for other_point in data_set:
		if math.dist(point.coords(), other_point.coords()) <= radius:
			neighbors.append(other_point)
	return neighbors

def core_point(number_of_neighbors, minimum_points):
	return number_of_neighbors >= minimum_points

def dbscan(data, epsilon, minimum_points):
	cluster_id = 0
	for point in data:
		if point.label is None:
			set_of_neighbors = range_query(data, point, epsilon)
			if not core_point(len(set_of_neighbors), minimum_points):
				point.set_label("Noise")
			else:
				cluster_label = f'cluster_{cluster_id}'
				point.set_label(cluster_label)
				set_of_neighbors.remove(point)
				for neighbor in set_of_neighbors:
					if neighbor.label == "Noise":
						neighbor.set_label(cluster_label)
					elif neighbor.label is None:
						next_set_of_neighbors = range_query(data, neighbor, epsilon)
						neighbor.set_label(cluster_label)
						if core_point(len(next_set_of_neighbors), minimum_points):
							set_of_neighbors.extend(next_set_of_neighbors)
				cluster_id += 1

dbscan(data_set, 1, 3)

num = 1
for point in data_set:
	print("point ", num, "label:", point.label, "coords: ", point.coords())
	num += 1
