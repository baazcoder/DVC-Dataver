import pandas as pd
import os

# CREATE A DATAFRAME
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
})

#adding new row to the dataframe
new_row = {'Name': 'simmi', 'Age': 29, 'City': 'San Francisco'}
df.loc[len(df)] = new_row

# making directory
output_dir = 'data'
os.makedirs(output_dir, exist_ok=True)
# SAVE THE DATAFRAME TO A CSV FILE
output_file = os.path.join(output_dir, 'output.csv')
df.to_csv(output_file, index=False)
# CHECK IF THE FILE EXISTS
if os.path.exists(output_file):
    print(f"The file '{output_file}' has been created successfully.")



