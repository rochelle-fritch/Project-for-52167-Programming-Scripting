# Project-for-52167-Programming-Scripting

## Final Project

### Background & data summary

The Iris dataset was collected by Edgar Anderson to investigate the morphologic variation of three classes (species) of Irises in Gaspé Peninsula (1). Fisher used this dataset in 1936 to discriminate between the classes (2). This multivariate data set records four variables of three classes of Iris (Iris Setosa, Iris Versicolour, Iris Virginica). Each class of Iris has 50 replicates, giving a total of 150 samples in the dataset. Four flower variables, as well as Iris class were recorded. Here each row representas a sample and each column represents a variable measured (3):

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



![alt text](https://github.com/rochelle-fritch/Project-for-52167-Programming-Scripting/blob/master/iris_output.png)
[CSV output file](https://github.com/rochelle-fritch/Project-for-52167-Programming-Scripting/blob/master/iris_output.png)

Graph Figure_1.png
![alt text](https://github.com/rochelle-fritch/Project-for-52167-Programming-Scripting/blob/master/Figure_1.png)
[Figure_1.png](https://github.com/rochelle-fritch/Project-for-52167-Programming-Scripting/blob/master/Figure_1.png)

