import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("fixed.csv")

pivot_table = df.pivot_table(index="State", columns="Condition Group", values="COVID-19 Deaths", aggfunc="sum")

plt.figure(figsize=(14, 8))
sns.heatmap(pivot_table, cmap="coolwarm", linewidths=0.5)
plt.title("Heatmap of COVID-19 Deaths by State & Condition Group", fontsize=14)
plt.xlabel("Condition Group")
plt.ylabel("State")
plt.show()
