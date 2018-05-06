# Project-for-52167-Programming-Scripting

## Final Project

### Background & data summary

The Iris dataset was collected by Edgar Anderson to investigate the morphologic variation of three classes (species) of Irises in Gaspé Peninsula (1). Fisher used this dataset in 1936 to discriminate between the classes (2). This multivariate data set records four variables of three classes of Iris (*Iris Setosa*, *Iris Versicolour*, *Iris Virginica*). Each class of Iris has 50 replicates, giving a total of 150 samples in the dataset. Four flower variables, as well as Iris class were recorded. Here each row representas a sample and each column represents a variable measured (3):

1.	sepal length (cm)
2.	sepal width (cm)
3.	petal length (cm)
4.	petal width (cm)
5.	Iris class 

This dataset is frequently used as a demonstration dataset for teaching basic programming for data analytics and machine learning. 

#### Exploration of data in python

First a dictionary was defined for the dataset called “iris_class”. This classified the three classes of iris and their samples for future use. Next, basic data exploration was executed using the Numpy library (4), this included minimum, maximum and mean (5) of each class of iris.

Both of these scripts were printed in the command line to check for errors. To allow for easier visualization, this data was then exported into a csv file (see attached iris_output.csv). 

Next the data was graphed, as a basic x,y plot, using the Matplotlib library (4, 5). First six individual figures were plotted for all combinations of sepal length, sepal width, petal length, petal width, as x,y plots. The three iris classes were plotted as three different colours. As this was cumbersome, all six plots were included in one figure, with one legend.

#### Results from data exploration

From this basic data exploration we can see the two classes of iris, *Iris versicolor* and *Iris virginica*, are morphologically similar, whereas *Iris setosa* is quite distinct (Figure 1, Table 1).

*I. setosa* has both a shorter sepal and petal length, smaller petals overall, in length and width, and wider sepals compared the two other classes. *I. versicolor* has slightly smaller petals in length and width compared to *I. virginica*.

##### Table 1. Showing the minumum, maximum and mean for sepal and petal length and width (S = Sepal, P = Petal, L = Length, W = Width) for three classes of iris.

Iris class      | SL Min | SL Max | SL Mean | SW Min | SW Max | SW Mean | PL Min | PL Max | PL Mean | PW Min | PW Max | PW Mean
:-------------: | :----: | :----: | :-----: | :----: | :----: | :-----: | :----: | :----: | :-----: | :----: | :----: | :-----:
Iris-setosa     | 4.3    | 5.8    | 5.006   | 2.3    | 4.4    | 3.418   | 1      | 1.9    | 1.464   | 0.1    | 0.6    | 0.244
Iris-versicolor | 4.9    | 7      | 5.936   | 2      | 3.4    | 2.77    | 3      | 5.1    | 4.26    | 1      | 1.8    | 1.326
Iris-virginica  | 4.9    | 7.9    | 6.588   | 2.2    | 3.8    | 2.974   | 4.5    | 6.9    | 5.552   | 1.4    | 2.5    | 2.026


[CSV output file](https://github.com/rochelle-fritch/Project-for-52167-Programming-Scripting/blob/master/iris_output.csv)


![alt text](https://github.com/rochelle-fritch/Project-for-52167-Programming-Scripting/blob/master/Figure_1.png)
##### Figure 1. Graph all combinations for three classes of iris. 
[Figure_1.png](https://github.com/rochelle-fritch/Project-for-52167-Programming-Scripting/blob/master/Figure_1.png)



### References

1.	[Anderson, E. (1936) The Species Problem in Iris. Annals of the Missouri Botanical Garden, 23, 457-509.](https://www.jstor.org/stable/2394164?seq=1#page_scan_tab_contents)
2.	[Fisher, R.A. (1936) The use of multiple measurements in taxonomic problems. Annals of Eugenics, 7, 179-188.](https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1469-1809.1936.tb02137.x)
3.	[Fisher, R.A. (1936) The Iris dataset.](http://archive.ics.uci.edu/ml/datasets/Iris)
4.	[NumPy](http://www.numpy.org/)
5.	[NumPy tutorial](https://docs.scipy.org/doc/numpy/user/quickstart.html)
6.	[Matplotlib](https://matplotlib.org/)
7.	[Matplotlib tutorial](https://matplotlib.org/tutorials/index.html)


