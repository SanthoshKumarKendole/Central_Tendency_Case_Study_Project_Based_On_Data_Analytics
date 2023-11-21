   # CENTRAL TENDENCY CASE STUDY PROJECT(Mean, Median, Mode)

import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as pt

data=pd.read_csv("C:/Users/KENDOLESANTHOSHKUMAR/Downloads/wine_quality.csv")
data.head(10)

data.shape

data.describe()

data.info()

data.columns

data.index

# Perform on Fixed Acidity

pt.figure(figsize=(10,6))
sb.histplot(data=data,x='fixed acidity',color='b',edgecolor='black',bins=6)
pt.title("Histogram on Fixed Aciditity")
pt.xlabel("Fixed acidity")
pt.ylabel("Count")
pt.show()

data['fixed acidity'].mean()

data['fixed acidity'].median()

pt.figure(figsize=(10,6))
sb.histplot(data=data,x='fixed acidity',color='b',edgecolor='black',bins=6)
pt.title("Histogram on Fixed Aciditity")
pt.xlabel("Fixed acidity")
pt.ylabel("Count")
pt.vlines(data['fixed acidity'].mean(),ymin=0,ymax=4000,label='Mean',color='red')
pt.vlines(data['fixed acidity'].median(),ymin=0,ymax=4000,label='Median',color='y')
pt.legend()
pt.show()

# Perform on Volatile Acidity

pt.figure(figsize=(10,6))
sb.histplot(data=data,x='volatile acidity',color='pink',bins=6,edgecolor='black')
pt.title("Histogram on Volatile Acidity")
pt.xlabel("Volatile Acidity")
pt.ylabel("Count")
pt.show()

pt.figure(figsize=(10,6))
sb.distplot(data['volatile acidity'])
pt.xlabel("Volatile Acidity")
pt.ylabel("Density")
pt.show()

data['volatile acidity'].skew()

data['volatile acidity'].mean()

data['volatile acidity'].median()

pt.figure(figsize=(10,6))
sb.histplot(data=data,x='volatile acidity',color='pink',edgecolor='black',bins=6)
pt.title("Histogram on Volatile Aciditity")
pt.xlabel("Volatile acidity")
pt.ylabel("Count")
pt.vlines(data['volatile acidity'].mean(),ymin=0,ymax=4000,label='Mean',color='red')
pt.vlines(data['volatile acidity'].median(),ymin=0,ymax=4000,label='Median',color='y')
pt.legend()
pt.show()

# Perform on Citric Acidity

pt.figure(figsize=(10,6))
sb.histplot(data=data,x='citric acid',bins=6,color='green',edgecolor='b')
pt.title("Histogram on Citric Acid")
pt.xlabel("Citric Acid")
pt.ylabel("Count")
pt.show()

pt.figure(figsize=(10,6))
sb.distplot(data['citric acid'])
pt.title("Distplot of Citric Acid")
pt.xlabel("Citric Acid")
pt.ylabel("Density")
pt.show()

data['citric acid'].mean()

data['citric acid'].median()

pt.figure(figsize=(10,6))
sb.histplot(data=data,x='citric acid',color='green',edgecolor='black',bins=6)
pt.title("Histogram on Citric Acidity")
pt.xlabel("Citric acidity")
pt.ylabel("Count")
pt.vlines(data['citric acid'].mean(),ymin=0,ymax=4000,label='Mean',color='red')
pt.vlines(data['citric acid'].median(),ymin=0,ymax=4000,label='Median',color='y')
pt.legend()
pt.show()

# Perform on Quality

data['quality'].value_counts()

data['quality'].value_counts().index[0]

data['quality'].value_counts().plot(kind='bar',color='y')
pt.title("Bar Graph of Quality")
pt.xlabel("Quality")
pt.ylabel("Count")
pt.show()

# Creating a Pandas Series

rep_acid=pd.Series(index=['fixed acidity','volatile acidity','citric acid','quality'],data=[data['fixed acidity'].mean(),data['volatile acidity'].mean(),data['citric acid'].mean(),data['quality'].value_counts().index[0]])

rep_acid

