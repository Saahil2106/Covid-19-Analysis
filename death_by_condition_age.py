import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("fixed.csv")

plt.figure(figsize=(14, 6))
sns.histplot(data=df, x="Age Group", hue="Condition Group", weights="COVID-19 Deaths", multiple="stack", palette="Set2")
plt.title("COVID-19 Deaths by Condition Group Across Age Groups", fontsize=14)
plt.xlabel("Age Group")
plt.ylabel("Total Deaths")
plt.xticks(rotation=45)
plt.show()
