# Understanding the Data Or work with any dataset using pandas in python
import pandas as pd

# 1. How big is the dataset ?
# 2. How does the data look likes ?
# 3. What is the datatypes of columns ?
# 4. Are there any missing values ?
# 5. How does the data look in mathematically ?
# 6. Are there duplicate values ?
# 7. How is the correlation between columns ?

# read csv
df = pd.read_csv("F:/github/ML-Basics/MLConcepts/Titanic-Dataset.csv")

# Ques 1 -> Using shape function check size of dataset
print(df.shape)
print()

# Ques 2 -> Using sample() function we can print the dataframe with random rows or we can use head() or tail() 
# for serial wise priniting from top or bottom
print(df.sample(4))
print()

# Ques 3 -> Using .info() function it will shows all the columns datatype with non-null value count
print(df.info())
print()
# For single column if you want to check the datatype use
print("Age datatype:-", df['Age'].dtype)
print()

# Ques 4 -> Using isnull() function we can check the null values in true or false form But if we want total count of null values for 
# each and specific col then use pd.isnull(df).sum()
# print(pd.isnull(df))
print(pd.isnull(df).sum())
print()

# Ques 5 -> Using describe() it will shows the main values using different formulas in mathematically form(such as-> mean, std, 25%) etc
print(df.describe())
print()

# Ques 6 -> Using duplicated().sum() the function shows the no of duplicate values
print("No. of duplicate values in row:", df.duplicated().sum())
print()

# Ques 7 -> Using corr() the function shows the correlation two each and every columns between -1 to 1 correlated 
numeric_df = df.select_dtypes(include=['number'])
v = numeric_df.corr()
print(v)