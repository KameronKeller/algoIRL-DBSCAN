# DBSCAN Script

## Scene 1: Premise

What is DBSCAN?

DBSCAN is a *density based* clustering algorithm. It finds areas in a data set with closely packed observations! 

Like you were probably going to guess... it also identifies areas with a low density of observations, and, isolates this *noise.*

The name kind of gets you there... **density based spatial clustering of applications with noise...**

Let's break that down a little...

1. Given a set of points in some n dimensional space,
2. find points that are closely packed together,
3. and, tag these areas as unique *clusters.*
4. The points that are not tightly packed together are outliers. These points without any close neighbors are considered *noise.*

So... why do we care that we can group together points into clusters?

---
## Scene 2: Present a problem (Applications of DBSCAN)

Say we want to.. recognize patterns..

Assuming the world is made up of distinct groups of objects that share properties we realize that some objects are more similar to each other than others.

It doesn't matter if we know "what" something is, it just matters that we can group it together with different things based on properties that can be measured.

This concept can be used in:
- Analyse imagery and determine **land use!**
- Find a protein's **docking sites!**
- Determine a berry's **ripeness!**
- Color **histograms!**
- Build a **recommender!**
- Identify **fake news!**
- Filter **things!**
- We can basically apply this anywhere patterns of similarity exist!

These applications typically fall into the bucket of unsupervised learning where a program can distinguish differences among objects (i.e. make clusters of similarities), but does not necessarily need to know "what" the objects are.

### Story

Our main character purchases flour from TraderShmoes. The store then sends our protagonist a list of coupons with great recommendations! They are ecstatic!

*scene props:*
- toilet paper
- masks
- and hand sanitizer
*end scene props*

TraderShmoes doesn't know the hero of this story, so how can they recommend things for them to buy?

Luckily TraderShmoes can "measure" what others have purchased and cluster all of those customers together based on their similar interests.

The cluster of products can represent an interest category of specific type of customer, so if one or more items from that cluster are purchased then some sort of conclusion can be made as to what else they might want.

---
## Scene 3: History/Legacy!

Why is DBSCAN used for these applications?

<!-- DBSCAN falls under a family of clustering algorithms.  -->

DBSCAN was published in in 1996 at the University of Munich. It was written by Martin Ester, Hans-Peter Kriegel, Jörg Sander, and Xiaowei Xu, with the goal of creating an improved cluster analysis algorithm. 

To understand the history of DBSCAN, we must begin with cluster analysis. Given a data set, it is not uncommon to find groupings (or clusters). Clusters help create classifications of data, which can then be analyzed and used to draw further conclusions. Cluster analysis was introduced in the 1930s in the field of anthropology and is frequently used in other scientific fields.

Many algorithms for identifying clusters in datasets exist, all with their pros and cons. However, algorithms for analyzing clusters in large datasets have the following goals:
1. Minimal knowledge about the domain.
    - For example, the k-means clustering algorithms requires the number of clusters to be specified in advance. But what if you do not know how many clusters to plan for?

2. Discovery of clusters with arbitrary shape.
    - Consider the following dataset. Notice how there are clearly two clusters. Using an algorithm like k-means might result in something that looks like this: 
    
    instead of this:


    (grab examples from: https://scikit-learn.org/0.15/auto_examples/cluster/plot_cluster_comparison.html)

3. Finally, cluster algorithms need "good efficiency" on large databases.

At the time of DBSCAN's publication, no clustering algorithm existed that satisfied all three of these requirements. DBSCAN met these requirements and provided a new way to analyze datasets.

---
## Scene 4. How does it work? (explanation)

Ok, so how exactly does DBSCAN work...

Let's think of DBSCAN like finding our neighbors in a neighborhood; or, core points in a cluster.

This algorithm steps through each point in the dataset and labels that point as a 
- **core point,**
- **border point,** or
- **noise point.**

There are two important parameters to determine what we label each point:
- `epsilon` and 
- `minimum_points`.

`epsilon` - defines the space to examine around each point.
- Say you are one point in the dataset. Who are your neighbors? They are the others living within a certain distance of you. So, if you reference one point in the dataset, these are the other points that are close to you. Let `epsilon`, define this shape around that one point.

`minimum_points` - provides us with a threshold from which to determine if a point is a **core point**, **border point**, or **noise point.**
- Considering that we have the shape, `epsilon`, established around us, count all your neighbors within that space. Now, we have a count of neighbors living within a certain space. Compare this count to the input: `minimum number of points`. 

Is the total number of neighbors within `epsilon`.. less than, equal to, or greater than `minimum_points`? and how does that map to the point's label type?

The algorithm labels each point comparing neighbor count to the `minimum_points` parameter.
- A *core point* is a point that has the same amount or more neighbors than the minimum points.
  
- A *noise point* is a point that has less than the minimum threshold aka `minimum_points`: `number of neighbor points` < `minimum_points`.

- A *border point* is a point that has less than the specified number of neighbors within the range, but is a neighbor of a **core point,** and still assigned to a cluster.

### explanation recap

To recap how DBSCAN works... 

There are two primary inputs:
- `epsilon` and,
- `minimum_points`

We step through and label every point in the dataset:

- If the number of points inside `epsilon` are greater than or equal to `minimum_points`, then that point is a **core point** (part of a cluster), 
  
- If the number of points inside `epsilon` is less than `minimum_points` then that point is either a **noise point**, 

- ...or a **border point**, iif it has a **core point** as a neighbor.

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

[Density-Based Cluster- and Outlier Analysis, Hans-Peter Kriegel](https://www.dbs.ifi.lmu.de/Forschung/KDD/Clustering/index.html)

[A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise, Martin Ester, Hans-Peter Kriegel, Jörg Sander, Xiaowei Xu](https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=5B7836C6FA0BBE6D059DE3E6E03C0428?doi=10.1.1.121.9220&rep=rep1&type=pdf)
