import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("fixed.csv")

plt.figure(figsize=(10, 6))
plt.scatter(df['COVID-19 Deaths'], df['Number of Mentions'], color='green', alpha=0.5)
plt.title('Scatterplot of COVID-19 Deaths vs. Number of Mentions', fontsize=14)
plt.xlabel('COVID-19 Deaths')
plt.ylabel('Number of Mentions')
plt.grid(True)
plt.tight_layout()
plt.show()
