# DBSCAN In Real Life

## Essence of DBSCAN
A clustering algorithm, groups data points that are in a specified proximity to each other

## History
An algorithm proposed by Martin Ester, Hans-Peter Kriegel, Jörg Sander, Xiaowei Xu in 1996 for class identification in spatial databases, which means grouping the objects of a database into sub categories.

>“However, the application to large spatial databases rises the following requirements for clustering algorithms: minimal requirements of domain knowledge to determine the input parameters, discovery of clusters with arbitrary shape and good efficiency on large databases. The well-known clustering algorithms offer no solution to the combination of these requirements.” (pg 1)

## Applications
DBSCAN can be useful when applied to a data set with multiple variables or *dimensions* that needs to be filtered into groups. This has importance in unsupervised learning applications.

> “The task considered in this paper is class identification, i.e. the grouping of the objects of a database into meaningful subclasses.” (pg 1)

## Key components
This algorithm attempts to label each point as one of the following:

1. **Core points** - data points that have a specified number of neighbors within a specified range.
   
2. **Border points** - data points that have *less* than the specified number of neighbors within the range.
   
3. **Noise points** - data points that have *no* neighboring points withing the range.
    
## Algorithm abstraction

### Inputs
- **setOfPoints** - multi dimensional data points
- **epsilon** - the distance where other points within this range can be neighbors
- **minimum points** - minimum number of neighbor points required for a point to be a core point

Other considerations:
- **ranging_method** - the formula to use for distance among data points
- **point_label** - the option to be a *core*, *border*, or *noise* point. 

### Steps
1. **For each point find neighbors in specified range**
   
2. **Create clusters with neighboring core points**
   
3. **For each non-core point:**
   - add to neighboring core point
   - *or* add to noise

## Pseudocode
- Input: `data`
- Input: `epsilon`
- Input: `minimum_points`
- Input: `ranging_method`
- Input: `point_label`
  
```ruby
clusters = []
# 1. Find neighbors
for each point in data
  if the point unlabeled?

    neighbors = range to(other points)

    # 2. Create cluster with core points
    if number of neighbors >= DENSITY_THRESHOLD?
      core_point = Core.new(point)
      cluster = Cluster.new().add(core_point)

    # 3. Non core points are noise or border points
    elsif number of neighbors is 1
      noise_point = Noise.new(point)
    else
      border_point = Border.new(point)
```
## Tools

[Visualizing DBSCAN Clustering](https://www.naftaliharris.com/blog/visualizing-dbscan-clustering/)

[Demo of DBSCAN clustering algorithm](https://notebooks.gesis.org/binder/jupyter/user/scikit-learn-scikit-learn-d7evzawb/lab/tree/notebooks/auto_examples/cluster/plot_dbscan.ipynb)

## References

https://dl.acm.org/doi/pdf/10.1145/3068335
