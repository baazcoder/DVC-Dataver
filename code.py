import pandas as pd
import os

# CREATE A DATAFRAME
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
})

# SAVE THE DATAFRAME TO A CSV FILE
output_file = 'output.csv'
df.to_csv(output_file, index=False)
# CHECK IF THE FILE EXISTS
if os.path.exists(output_file):
    print(f"The file '{output_file}' has been created successfully.")



