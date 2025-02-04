import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def clean_and_explore_data(input_file, output_file):
    df = pd.read_csv(input_file)
    
    df['Year'] = df['Year'].fillna(method='ffill').fillna(df['Year'].mode()[0])
    df['Month'] = df['Month'].fillna(method='ffill').fillna(df['Month'].mode()[0])
    
    df['Number of Mentions'] = df['Number of Mentions'].apply(lambda x: x if x > 0 else df['Number of Mentions'].median())
    
    df.drop(columns=['Flag'], inplace=True)
    if 'Row Number' in df.columns:
        df.drop(columns=['Row Number'], inplace=True)
    
    df.to_csv(output_file, index=False)
    print(f"Cleaned and explored data saved to {output_file}")

input_file = "covid19_death_conditions.csv"
output_file = "covid19_death_conditions_cleaned.csv"
clean_and_explore_data(input_file, output_file)
