import pandas as pd

"""if you want to display all columns and rows use below lines"""
pd.set_option("display.max_columns", None)
# pd.set_option("display.max_rows", None) #shows all rows, for efficiency comment line because of vast data

"""below lines is actually to read the csv file from current file"""
df = pd.read_csv("diamonds.csv")
print(df)
print("---------------------------------------------")

"""below lines is actually to read only columns names"""
column = df.columns
print(column)
print("----------------------------------------------")

"""below lines is actually to read the data types of the given dataset"""
column_data_types = df.dtypes
print(column_data_types)
print("----------------------------------------------")

"""output: overall dtypes:object
prefernce for dtypes to display in this order
 --->object(string)
 --->float
 --->integer
 python display even if one object present, it shows object only"""

"""below lines is to get the general information about the dataset"""
df_information = df.info() # parantheses represents the function or method
print(df_information)
print("***************************************")

"""below function will work only on the numerical columns"""
df_description = df.describe()

print(df_description)

finding_null = df.isna()
print(finding_null)

cut_column_detailing = df["cut"].unique()
print(cut_column_detailing)