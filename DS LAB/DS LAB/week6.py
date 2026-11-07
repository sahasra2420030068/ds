import pandas as pd
from sklearn.datasets import load_iris
from statistics import mode
#load iris dataset
iris=load_iris()
df=pd.DataFrame(data=iris.data,columns=iris.feature_names)
print("First 5 rows of dataset:")
print(df.head())
#Mean(average)
mean_values=df.mean()
print("Mean values:")
print(mean_values)
#Median(middle value)
median_values=df.median()
print("Median values:")
print(median_values)
#Mode(most frequent value)
#pandas mode returns a dataframe(can be multiple modes)
mode_values=df.mode().iloc[0]
print("Mode values:")
print(mode_values)


import pandas as pd
# Load tips dataset
df = pd.read_csv("tips.csv")
print("First 5 rows of dataset:")
print(df.head())
# Mean (average)
mean_values = df.mean(numeric_only=True)
print("\nMean values:")
print(mean_values)
# Median (middle value)
median_values = df.median(numeric_only=True)
print("\nMedian values:")
print(median_values)
# Mode (most frequent value)
mode_values = df.mode().iloc[0]
print("\nMode values:")
print(mode_values)



#to calculate range and variance
import pandas as pd
from sklearn.datasets import load_iris
#load iris dataset
iris=load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
print("First 5 rows of dataset:")
print(df.head())
#Range (max-min)
range_values=df.max()-df.min()
print("Range values:")
print(range_values)
#Variance
variance_values=df.var()
print("Variance values:")
print(variance_values)
#Standard Deviation
std_values=df.std()
print("Standard Deviation values:")
print(std_values)
#interquartile range(IQR)
Q1=df.quantile(0.25)
Q3=df.quantile(0.75)
IQR=Q3-Q1
print("Interquartile Range (IQR):")
print(IQR)



# To calculate Range, Variance, Standard Deviation and IQR
import pandas as pd
# Load tips dataset
df = pd.read_csv("tips.csv")
print("First 5 rows of dataset:")
print(df.head())
# Range (max - min)
range_values = df.max(numeric_only=True) - df.min(numeric_only=True)
print("Range values:")
print(range_values)

# Variance
variance_values = df.var(numeric_only=True)
print("Variance values:")
print(variance_values)
# Standard Deviation
std_values = df.std(numeric_only=True)
print("Standard Deviation values:")
print(std_values)
# Interquartile Range (IQR)
Q1 = df.quantile(0.25, numeric_only=True)
Q3 = df.quantile(0.75, numeric_only=True)
IQR = Q3 - Q1
print("Interquartile Range (IQR):")
print(IQR)



#how data got distributed
import pandas as pd
from sklearn.datasets import load_iris
#load iris dataset
iris=load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
print("First 5 rows of dataset:")
print(df.head())
#Skewness(asymmetry of distribution)
skewness_values=df.skew()
print("Skewness values:")
print(skewness_values)
#Kurtosis(peakedness /tail heaviness)
kurtosis_values=df.kurtosis()
print("Kurtosis values:")
print(kurtosis_values)

# How data got distributed
import pandas as pd
# Load tips dataset
df = pd.read_csv("tips.csv")
print("First 5 rows of dataset:")
print(df.head())
# Skewness (asymmetry of distribution)
skewness_values = df.skew(numeric_only=True)
print("Skewness values:")
print(skewness_values)
# Kurtosis (peakedness / tail heaviness)
kurtosis_values = df.kurtosis(numeric_only=True)
print("Kurtosis values:")
print(kurtosis_values)



