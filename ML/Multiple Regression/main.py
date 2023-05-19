import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
boston_datasets = pd.DataFrame(data,
                               columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
                                        'PTRATIO', 'B',
                                        'LSTAT'])

# print(len(boston_datasets))
for i in range(len(boston_datasets)):
    boston_datasets.at[i, "PRICE"] = random.randint(20, 100)

# Checking the top part of the dataset
# print(boston_datasets.head())

# Checking the bottom part of the dataset.
# print(boston_datasets.tail())


# Checking if there is any null value in the columns of the datasets.

# print(pd.isnull(boston_datasets).any())

# plt.hist(boston_datasets["PRICE"], bins=30, ec='yellow')
# plt.xlabel("Price in thousands", labelpad=10)
# plt.ylabel("No. of houses", labelpad=10)
# sns.histplot(boston_datasets["PRICE"], bins=30)
# plt.xlabel("Price in thousands", labelpad=10)
# plt.ylabel("No. of houses", labelpad=20)
# average = boston_datasets["RM"].mean()
# print(average)

# plt.hist(boston_datasets["RAD"], bins=30, ec='yellow')
# plt.xlabel("Highways accessibility", labelpad=10)
# plt.ylabel("No. of houses", labelpad=10)
count = 0
all_values = boston_datasets["CHAS"].values
for i in range(len(all_values)):
    if all_values[i] == 1:
        count += 1

print("The number of houses beside the river ", count)
corr = boston_datasets["PRICE"].corr(boston_datasets["RM"])
print(corr)
corr = boston_datasets["PRICE"].corr(boston_datasets["PTRATIO"])
print(corr)
plt.show()
