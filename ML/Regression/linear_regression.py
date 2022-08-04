import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pandas.read_csv("cost_revenue_clean.csv")
# This gives us max, min, count and other stuffs about data.
print(data.describe())

font1 = {'family': 'serif',
         'color': 'blue',
         'size': 10
         }
font2 = {'family': 'serif',
         'color': 'darkred',
         'size': 12
         }


plt.figure(figsize=(10, 6))
plt.xlabel("Production_Budget", fontdict=font1)
plt.ylabel("Worldwide_Gross_Budget", fontdict=font1)
plt.title("Production Budget Vs Worldwide Gross Budget", fontdict=font2)

X = pandas.DataFrame(data, columns=["production_budget"])
Y = pandas.DataFrame(data, columns=["worldwide_gross_budget"])
plt.scatter(X, Y, alpha=.4)
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)

regression = LinearRegression()

regression.fit(X, Y)
print(regression.coef_)         # Slope of the graph.
print(regression.intercept_)    # Intercept of the graph

# This line plots the line on the graph. Here we are using the value of X as X because we are using it as
# independent variable. We are using the same X value we are getting from the csv sheet. Now, if we use the same value Y
# value of the sheet it would not make any sense. So, in order to have relationship between these two variables we are
# going to use the X values to get the predicted Y values. We already know the slope and intercept
# from X and previous Y value.

# This line will plot the graph on the background.
plt.plot(X, regression.predict(X), color="green", linewidth=3)
print(regression.score(X, Y))
# We need this line to show the graph on the screen.
plt.show()

