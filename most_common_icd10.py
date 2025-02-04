import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("fixed.csv")

icd_deaths = df.groupby("ICD10_codes")["COVID-19 Deaths"].sum().reset_index()
icd_deaths = icd_deaths.sort_values(by="COVID-19 Deaths", ascending=False).head(15)

plt.figure(figsize=(12, 6))
sns.barplot(x="COVID-19 Deaths", y="ICD10_codes", data=icd_deaths, palette="magma")
plt.title("Top 15 Most Common ICD-10 Conditions Contributing to Deaths", fontsize=14)
plt.xlabel("Total Deaths")
plt.ylabel("ICD-10 Code")
plt.show()
