import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("fixed.csv")

age_group_deaths = df.groupby("Age Group")["COVID-19 Deaths"].sum().reset_index()
age_group_deaths = age_group_deaths.sort_values(by="COVID-19 Deaths", ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x="COVID-19 Deaths", y="Age Group", data=age_group_deaths, palette="Blues_r")
plt.title("Total COVID-19 Deaths by Age Group", fontsize=14)
plt.xlabel("Total Deaths")
plt.ylabel("Age Group")
plt.show()
