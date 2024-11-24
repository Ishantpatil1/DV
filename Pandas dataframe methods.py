# Importing the necessary libraries
import pandas as pd
import numpy as np

# Creating the DataFrame with specified data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice', 'Eve'],
    'Age': [25.0, 30.0, 35.0, 40.0, 25.0, np.nan],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'New York', 'Los Angeles']
}
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:\n", df)

# 1. Count the non-null entries
count_non_null = df.count()
print("\nCount of Non-Null Entries:\n", count_non_null)

# 2. Describe the DataFrame
description = df.describe(include='all')
print("\nStatistical Description:\n", description)

# 3. Drop duplicates
df_dropped_duplicates = df.drop_duplicates()
print("\nDataFrame After Dropping Duplicates:\n", df_dropped_duplicates)

# 4. Check whether the DataFrame is empty
is_empty = df.empty
print("\nIs the DataFrame Empty?:", is_empty)

# 5. Filter records containing City as 'New York'
filtered_ny = df[df['City'] == 'New York']
print("\nFiltered Records with City as 'New York':\n", filtered_ny)

# 6. Create a copy of the DataFrame and compare
df_copy = df.copy()
are_equal = df.equals(df_copy)
print("\nAre the Original and Copied DataFrame Equal?:", are_equal)
