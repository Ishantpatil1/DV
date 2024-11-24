# Importing libraries
import pandas as pd
import numpy as np

# Creating a DataFrame
data = {
    'Name': ['Saransh', 'Shiwali', 'Shivansh', 'Sukruti', 'Shaan'],
    'Age': [19, 20, 25, 22, 23],
    'City': ['New Delhi', 'Banglore', 'Hyderabad', 'Mumbai', 'Pune']
}
df = pd.DataFrame(data)

# Display the DataFrame
print("Initial DataFrame:")
print(df)

# Display the first few rows
print("\nFirst few rows of the DataFrame:")
print(df.head())

# Display basic information about the DataFrame
print("\nDataFrame Information:")
df.info()

# Summary statistics of numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Add a new column with age in months
df['Age_in_Months'] = df['Age'] * 12
print("\nDataFrame with 'Age_in_Months':")
print(df)

# Filter rows where Age is less than 30
filtered_df = df[df['Age'] < 30]
print("\nFiltered DataFrame (Age < 30):")
print(filtered_df)

# Sort ages in ascending order
sorted_df = df.sort_values(by='Age')
print("\nDataFrame sorted by Age (ascending):")
print(sorted_df)

# Introduce a missing value
df.loc[2, 'City'] = np.nan
print("\nDataFrame with missing value:")
print(df)

# Fill missing values with 'Unknown'
df['City'] = df['City'].fillna('Unknown')
print("\nDataFrame after filling missing values:")
print(df)

# Save DataFrame to CSV
df.to_csv('manipulated_data.csv', index=False)
print("\nDataFrame saved to 'manipulated_data.csv'.")

# Creating a Series from a list
data_list = [10, 20, 30, 40, 50]
series_list = pd.Series(data_list, name='Values')
print("\nSeries created from a list:")
print(series_list)

# Creating a Series from a dictionary
data_dict = {'A': 100, 'B': 200, 'C': 300, 'D': 400}
series_dict = pd.Series(data_dict, name='Scores')
print("\nSeries created from a dictionary:")
print(series_dict)

# Accessing data by integer index
value_at_index_2 = series_list[2]
print("\nValue at index 2 in series_list:", value_at_index_2)

# Accessing data by label
score_A = series_dict['A']
print("\nScore for label 'A' in series_dict:", score_A)


