# DBSCAN Script

## 1. Premise

What is DBSCAN?

DBSCAN is a *density based* clustering algorithm. It finds areas in a data set with a high density of observations! 

Like you were probably going to guess... it also determines areas with a low density of observations, and, isolates this *noise.*

It kind of gets you there with the name - **density based spatial clustering of applications with noise...**

Let's break that down a little...

1. Given a set of points in some n dimensional space
2. Points that are closely packed together
3. Tag as unique *clusters*
4. The points that are not tightly packed together are outliers. These points without any close neighbors are considered *noise*.

So... why do we care that we can group together points into clusters?

## 2. Present a problem (Applications of DBSCAN)

Say we want to.. 

- accomplish x with unsupervised learning

## 3. History/Legacy!
DBSCAN falls under a family of clustering algorithms.

## 4. Solve the problem

## 5. How does it work? (meat and potatoes)
The algorithm has two adjustable parameters, the *minimum number of points* that fall within a certain *radius* of a point. This allows us control over the density of the clusters.

Let `radius`  be the radius of a neighborhood with respect to some point, and let `min_points` be the required minimum number of points needed to make a neighborhood a neighborhood.

Then we will have as follows:
- A *core point* is a point that has a required number of neighbors, `neighbors` >= `min_points`
- A *noise point* is a point that has less than the required number of neighbors.

## Let's recap that:

DBSCAN attempts to label each point as one of the following:

Core points - data points that have a specified number of neighbors within a specified range.

Border points - data points that have less than the specified number of neighbors within the range.

Noise points - data points that have no neighboring points withing the range.

## 6. Computer speak: pseudocode

## 6. Summary
