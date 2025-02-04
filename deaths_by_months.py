import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("fixed.csv")

plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x="Month", y="COVID-19 Deaths", palette="coolwarm")
plt.title("COVID-19 Deaths by Month", fontsize=14)
plt.xlabel("Month")
plt.ylabel("COVID-19 Deaths")
plt.show()
