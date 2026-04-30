PROBLEM STATEMENT:
a. Write Program to Load, Clean and Exploring the data using python
b. Write a Program to implement various types of visualization in python

AIM:
To implement different types of data visualization using Python

ALGORITHM:
Start
Import pandas and matplotlib
Load dataset
Create line plot
Create bar chart
Create histogram
Create scatter plot
Create box plot
Display plots
Stop

code:
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

data.iloc[:, 0:2].plot()
plt.title("Line Plot")
plt.show()

data.iloc[:, 0].value_counts().plot(kind='bar')
plt.title("Bar Chart")
plt.show()

data.hist()
plt.title("Histogram")
plt.show()

plt.scatter(data.iloc[:, 0], data.iloc[:, 1])
plt.title("Scatter Plot")
plt.show()

data.plot(kind='box')
plt.title("Box Plot")
plt.show()

output:
   Age  Salary  Experience
0   25   50000           2
1   30   60000           5
2   22   45000           1
3   28   52000           3
4   35   65000           7

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
Age           int64
Salary        int64
Experience    int64

             Age   Salary  Experience
count   5.000000  5.000000   5.000000
mean   28.000000 54400.000000 3.600000
min    22.000000 45000.000000 1.000000
max    35.000000 65000.000000 7.000000

Age           0
Salary        0
Experience    0

Age           0
Salary        0
Experience    0

                Age    Salary  Experience
Age         1.000000  0.980580   0.981981
Salary      0.980580  1.000000   0.997054
Experience  0.981981  0.997054   1.000000
