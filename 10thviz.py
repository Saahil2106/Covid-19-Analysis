import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("fixed.csv")

df["Start Date"] = pd.to_datetime(df["Start Date"])

df_grouped_condition = df.groupby("Condition")["Number of Mentions"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
df_grouped_condition.plot(kind='bar', color='teal')
plt.xlabel("Condition")
plt.ylabel("Number of Mentions")
plt.title("Top 10 Most Mentioned Conditions")
plt.xticks(rotation=75)
plt.show()
