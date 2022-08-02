import pandas as pd
import math

pd.options.mode.chained_assignment = None  # default='warn'

data = pd.read_csv("lsd_math_score_data.csv")
# print(type(data))

data["Higher_Score"] = 100
# print(data)

for high_score in range(len(data["Higher_Score"])):
    data["Higher_Score"][high_score] = data["Avg_Math_Test_Score"][high_score] + 100

for high_score in range(len(data["Higher_Score"])):
    data["Higher_Score"][high_score] *= data["Higher_Score"][high_score]

# print(data)

lsd_ppm = list(data["LSD_ppm"])
avg_math_score = list(data["Avg_Math_Test_Score"])
# print(lsd_ppm)
# print(avg_math_score)

clean_data = {'LSD_ppm': lsd_ppm, 'Avg_Math_Test_Score': avg_math_score}

df = pd.DataFrame(clean_data)
# print(df)
del data["Higher_Score"]
# print(data)

e = math.e
print(e)