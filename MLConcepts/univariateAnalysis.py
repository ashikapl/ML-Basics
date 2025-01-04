# Univariate Analysis -> Work with single colums in categorical and numerical data
# Data -> Two Types -> Categorical and Numerical Data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("F:/github/ML-Basics/MLConcepts/Titanic-Dataset.csv")
# print(df.columns)
# print(df.info())

# Categorical Data -> 'Survived', 'Pclass', 'Sex', 'Embarked', 'Name'(With the many categories)
# 1-> Countplot -> Frequency Count
sns.countplot(data=df, x='Survived')
plt.title("Passenger Survival Count")
plt.show()

sns.countplot(data=df, x='Pclass')
plt.title("Pclass Count")
plt.show()

sns.countplot(data=df, x='Embarked')
plt.title("Embraked Count")
plt.show()

# Numerical Data -> 'PassengerId', 'Age', 'SibSp', 'Cabin'(lot of values), 'Parch', 'Ticket'(May be its Categorical), 'Fare'
# 2-> Histogram -> for continuous data
# distplot is remove from the updated seaborn library only use kde(kernal Density Estimation) to draw a line on the graph
sns.histplot(data=df, x='Age', kde=True)
plt.title("Age Plot")
plt.show()

sns.histplot(data=df, x='SibSp', kde=True)
plt.title("SibSp Plot")
plt.show()

sns.histplot(data=df, x='Parch', kde=True)
plt.title("Parch Plot")
plt.show()

sns.histplot(data=df, x='Fare', kde=True)
plt.title("Fare Plot")
plt.show()

# Boxplot searching for outliers
sns.boxplot(data=df, x='Age')
plt.title("Age BoxPlot for outliers")
plt.show()

sns.boxplot(data=df, x='SibSp')
plt.title("SibSp BoxPlot for outliers")
plt.show()

sns.boxplot(data=df, x='Parch')
plt.title("Parch BoxPlot for outliers")
plt.show()

sns.boxplot(data=df, x='Fare')
plt.title("Fare BoxPlot for outliers")
plt.show()
