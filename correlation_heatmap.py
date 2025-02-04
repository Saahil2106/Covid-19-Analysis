import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("fixed.csv")

numeric_df = df.select_dtypes(include=['float64', 'int64'])

plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap of COVID-19 Dataset", fontsize=14)
plt.show()
