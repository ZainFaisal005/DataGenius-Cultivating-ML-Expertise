import pandas as pd
import numpy as np

# Sample dataset with missing values
data = {
    "A": [1, 2, np.nan, 4, 5],
    "B": [3, np.nan, 6, 7, 8],
    "C": [9, 10, 11, np.nan, 13],
}
df = pd.DataFrame(data)


def fill_missing_with_mean(df):
    return df.fillna(df.mean())


def fill_missing_with_median(df):
    return df.fillna(df.median())


def fill_missing_with_mode(df):
    return df.apply(lambda x: x.fillna(x.mode()[0]))


print("Original DataFrame:")
print(df)

print("\nDataFrame after filling missing values with mean:")
print(fill_missing_with_mean(df))

print("\nDataFrame after filling missing values with median:")
print(fill_missing_with_median(df))

print("\nDataFrame after filling missing values with mode:")
print(fill_missing_with_mode(df))
