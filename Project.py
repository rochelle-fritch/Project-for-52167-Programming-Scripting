# Rochelle Fritch 
# Project for 52167-Programming-Scripting



import numpy as np # import the package and make a shortcut "np"
import matplotlib.pyplot as plt

# Using the week 5 assignment as a starting point.

# Here we are defining the dictionary to use after. 

iris_class = {}     # defines the dictionary
with open("Data/iris.csv") as f:
    for line in f:                          # looping through each line in file
        if line[-1] == '\n':                # removes the last charater for each line
            line = line[:-1]
        x = line.split(',')                 # splits lines into a list, read the line
        dat = [float(i) for i in x[:-1]]    # defines floating point number, comprehension list, exept for the last item, which is a string.
        if x[4] in iris_class:              
            iris_class[x[4]].append(dat)    # Index "iris class" by the class of the current line. 
        else :
            iris_class[x[4]] = [dat]   
print(iris_class)                           # This prints the dictionary created above (looks ugly, but I have done to visualise the list)

# This prints the minimum, maximum and mean for each class of Iris, each on it's own line for: sepal length, sepal width, petal length, petal width.

for k,v in iris_class.items():     # k is class name, v is the all data for this class. items is a list with k & v
    v = np.array(v).transpose()    # transpose the column and row
    dat = []
    for i in v:                    # computing the value of each
        dat.append(str(i.min()))   # str = string
        dat.append(str(i.max()))
        dat.append(str(i.mean()))
    print(k+", "+", ".join(dat))


# This is a print out of the above in a csv, with labels for each column.

with open("Data/iris_output.csv", "w") as f:        # w = write (default is r = read)
    f.write("Iris class, SL Min, SL Max, SL Mean, SW Min, SW Max, SW Mean, PL Min, PL Max, PL Mean, PW Min, PW Max, PW Mean\n") # S = Sepal, P = Petal, L = Length, W = Width
    for k,v in iris_class.items():     # k is class name, v is the all data for this class. items is a list with k & v
        v = np.array(v).transpose()    # transpose the column and row
        dat = []
        for i in v:                     # computing the value of each
            dat.append(i.min())         # remove the string, so that it is a number
            dat.append(i.max())
            dat.append(i.mean())
        f.write(("{}"+", {}"*12+"\n").format(k, *dat))  # This allows formatting for each variable, the class is 1st, with the other as *12.

# Plottting six scatter plots for correlations of Sepal and Petal lenth

fig, ax = plt.subplots(2, 3)                            # Putting plots in 2 rows and 3 colmns. 
ax = ax.ravel()                                         # flattens an ray to 1 line
lab = ['Sepal length (cm)', 'Sepal width (cm)','Petal length (cm)', 'Petal width (cm)']    # labels for x, y axes
i = 0                                                   # number for indexingthe plot
for ix, iy in [ (0,1), (0,2), (0,3), (1,2), (1,3), (2,3) ]:
    axi = ax[i]
    for k,v in iris_class.items():                      # k is class name, v is the all data for this class. items is a list with k & v
        v = np.array(v).transpose()                     # transpose the column and row
        axi.plot(v[ix], v[iy], "o", label=k)            # This is for a circle plot
    axi.set_xlabel(lab[ix])
    axi.set_ylabel(lab[iy])
    i += 1
ax[0].legend()                                          # legand only once at 0
plt.show()                                              # This visualises the plot that you have just made, this stops the script, but you need to close the figure first. 

        