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

---
## Scene 2: Present a problem (Applications of DBSCAN)

Say we want to.. recognize patterns..

Assuming the world is made up of distinct groups of objects that share properties we realize that some objects are more similar to each other than others.

It doesn't matter if we know "what" something is, it just matters that we can group it together with different things based on properties that can be measured.

This concept can be used to:
- Determine a berry's **ripeness!**
- Build a **recommender!**
- Identify **fake news!**
- Filter **things!**
- We can basically apply this anywhere patterns of similarity exist!

---
## Scene 3: History/Legacy!

Why is DBSCAN used for these applications?

DBSCAN falls under a family of clustering algorithms. 

<!-- add history, importance, etc -->

---
## Scene 4. How does it work? (explanation)

Ok, so how exactly does DBSCAN work...

Let's use a *recommender* example to walk through this.

The algorithm has two adjustable parameters, the *minimum number of points* that fall within a certain *radius* of a point. This allows us control over the density of the clusters.

Let `radius`  be the radius of a neighborhood with respect to some point, and let `min_points` be the required minimum number of points needed to make a neighborhood a neighborhood.

Then we will have as follows:
- A *core point* is a point that has a required number of neighbors, `neighbors` >= `min_points`
- A *noise point* is a point that has less than the required number of neighbors.

DBSCAN attempts to label each point as one of the following:

Core points - data points that have a specified number of neighbors within a specified range.

Border points - data points that have less than the specified number of neighbors within the range.

Noise points - data points that have no neighboring points withing the range.

## Scene 6. Pseudocode

<!-- write a script talking through the pseudocode, may be best to get a solid version of our pseudocode first and simplify it a little -->

<!-- Here's a web app that might help -->
[slides code highlighter](https://romannurik.github.io/SlidesCodeHighlighter/)

## Scene 7. Complexity

DBSCAN checks for neighbors within the n dimensional shape around each point in the data. This checking process takes O(n^2).

<!-- detailed analysis / complexity equation? => simplifies down to O(n^2) -->

## Scene 8. Summary

Let's recap that...

<!-- add summary of DBSCAN concepts -->
 
 ## Scene 9. References

<!-- add references here -->

