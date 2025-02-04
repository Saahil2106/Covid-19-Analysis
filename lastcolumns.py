import pandas as pd

file_path = "covid19_death_conditions_cleaned.csv"  
df = pd.read_csv(file_path)

df.fillna(0, inplace=True)

cleaned_file_path = "fixed.csv"  
df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned file saved as: {cleaned_file_path}")
