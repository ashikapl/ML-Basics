# Bivariate and MultiVariate Analysis
# There are three types of relations -> 1.Numerical-Numerical, 2.Categorical-Categorical, 3.Numerical-Categorical
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("F:/github/ML-Basics/MLConcepts/Titanic-Dataset.csv")
# print(df.head())

# Categorical col -> ['Survived', 'Parch', 'Pclass', 'Name', 'Sex', 'Embarked']
# Numerical col -> ['PassengerId', 'Ticket', 'Fare', 'Cabin', 'SibSp', 'Age'],

# Numerical-Numerical (multiVariate Analysis) comparing two or more columns
sns.scatterplot(x='Age',y='Fare',data=df,hue='Sex',style='Parch',size='Embarked')
plt.show()

# Numerical-Categorical (Bivariate Analysis) comparing two columns
sns.barplot(x='Sex',y='Survived',data=df)
plt.show()

# Numerical-Categorical boxplot is used for outlier visualizing
sns.boxplot(x='Survived',y='Age',data=df)
plt.show()

# Numerical-Categorical distplot can also use in this type
sns.displot(x='Age',hue='Survived',data=df,kind='kde')
plt.show()

# Categorical-Categorical 
sns.heatmap(pd.crosstab(df['Pclass'],df['Survived']))
plt.show()

# Categorical-Categorical # clustermal is work like a dendogram 
sns.clustermap(pd.crosstab(df['Sex'],df['Embarked']))
plt.show()

# Numerical-Numerical # pairplot shows all numerical col correlation with each other
sns.pairplot(data=df)
plt.show()

# Numerical-Numerical 
sns.lineplot(x='SibSp',y='Fare',data=df)
plt.show()
# print(df.info())