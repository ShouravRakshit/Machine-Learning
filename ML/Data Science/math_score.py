import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'

data = pd.read_csv("lsd_math_score_data.csv")
# print(type(data))

data["Higher_Score"] = 100
# print(data)

for high_score in range(len(data["Higher_Score"])):
    data["Higher_Score"][high_score] = data["Avg_Math_Test_Score"][high_score] + 100

for high_score in range(len(data["Higher_Score"])):
    data["Higher_Score"][high_score] *= data["Higher_Score"][high_score]

print(data)

# lsd_ppm = list(data["LSD_ppm"])
# avg_math_score = list(data["Avg_Math_Test_Score"])
# print(lsd_ppm)
# print(avg_math_score)

# clean_data = {'LSD_ppm': lsd_ppm, 'Avg_Math_Test_Score': avg_math_score}

# df = pd.DataFrame(clean_data)
# print(df)
# del data["Higher_Score"]
# print(data)

title_font = {
    "fontsize": 15,
    "color": "orange",
    "horizontalalignment": "center"
}

x_label_font = {
    "fontsize": 15,
    "color": "blue",
    "horizontalalignment": "center"
}

y_label_font = {
    "fontsize": 15,
    "color": "blue",
    "horizontalalignment": "center"
}

# e = math.e

plt.figure(figsize=(7, 7))
time_delay_minutes = data[["Time_Delay_in_Minutes"]]
lsd_ppm = data[["LSD_ppm"]]
avg_math_score = data[["Avg_Math_Test_Score"]]

x = np.array(lsd_ppm)
y = np.array(avg_math_score)
# print([x])
# print(y)
regression = LinearRegression()
# To get the fit of the graph we need independent and dependant variable.
regression.fit(x, y)
print(regression.coef_)         # Slope of the graph.
print(regression.intercept_)    # Intercept of the graph.
print(regression.score(x, y))
plt.title(label="Tissue concentration of LSD over time", fontdict=title_font)
plt.xlabel(xlabel="LSD (ppm)", fontdict=x_label_font)
plt.ylabel(ylabel="Math Score", fontdict=y_label_font)
plt.text(x=0, y=.3, s="Wagner et al. (1968)")
plt.plot(x, y, color="red", linewidth=4)
plt.show()
