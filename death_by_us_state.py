import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("fixed.csv")

df = df[df["State"] != "United States"]

state_deaths = df.groupby("State")["COVID-19 Deaths"].sum().reset_index()
state_deaths = state_deaths.sort_values(by="COVID-19 Deaths", ascending=False).head(20)

plt.figure(figsize=(12, 6))
sns.barplot(x="COVID-19 Deaths", y="State", data=state_deaths, palette="Greens_r")
plt.title("Top 20 States with Highest COVID-19 Deaths", fontsize=14)
plt.xlabel("Total Deaths")
plt.ylabel("State")
plt.show()
