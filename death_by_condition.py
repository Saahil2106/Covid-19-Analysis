import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("fixed.csv")

condition_deaths = df.groupby("Condition Group")["COVID-19 Deaths"].sum().reset_index()
condition_deaths = condition_deaths.sort_values(by="COVID-19 Deaths", ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x="COVID-19 Deaths", y="Condition Group", data=condition_deaths, palette="Reds_r")
plt.title("COVID-19 Deaths by Condition Group", fontsize=14)
plt.xlabel("Total Deaths")
plt.ylabel("Condition Group")
plt.show()
