# DBSCAN Script

## Scene 1: Premise

What is DBSCAN?

DBSCAN is a *density based* clustering algorithm. It finds areas in a data set with closely packed observations! 

Like you were probably going to guess... it also identifies areas with a low density of observations, and, isolates this *noise.*

The name kind of gets you there... **density based spatial clustering of applications with noise...**

Let's break that down a little...

1. Given a set of points in some n dimensional space,
2. then, find points that are closely packed together,
3. and, tag these areas as unique *clusters.*
4. The points that are not tightly packed together are outliers. These points without any close neighbors are considered *noise*.

So... why do we care that we can group together points into clusters?

## Scene 2: Present a problem (Applications of DBSCAN)

Say we want to.. teach a computer to recognize patterns!

Assuming the world is made up of distinct groups of objects that share properties

We realize that some objects are more similar to each other than others.

This concept can be used to:
- Expose **fraudulent activity!**
- Filter **spam!**
- Build a **recommender!**
- Identify **fake news!**
- We can basically apply this anywhere patterns of similarity exist!

## Scene 3: History/Legacy!
DBSCAN falls under a family of clustering algorithms.

## Scene 4: Solve the problem

## 5. How does it work? (meat and potatoes)

Ok, so how exactly does this work...

The algorithm has two adjustable parameters, the *minimum number of points* that fall within a certain *radius* of a point. This allows us control over the density of the clusters.

Let `radius`  be the radius of a neighborhood with respect to some point, and let `min_points` be the required minimum number of points needed to make a neighborhood a neighborhood.

Then we will have as follows:
- A *core point* is a point that has a required number of neighbors, `neighbors` >= `min_points`
- A *noise point* is a point that has less than the required number of neighbors.

DBSCAN attempts to label each point as one of the following:

Core points - data points that have a specified number of neighbors within a specified range.

Border points - data points that have less than the specified number of neighbors within the range.

Noise points - data points that have no neighboring points withing the range.

## 6. Computer speak: pseudocode

## 6. Summary

Let's recap that...

