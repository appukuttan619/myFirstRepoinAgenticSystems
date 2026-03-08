import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Julia"],
    "Age": [24, 27, 22, 32, 29, 35, 28, 26, 31, 23],
    "Score": [88, 76, 95, 67, 82, 91, 73, 85, 79, 92],
    "Label": ["Pass", "Pass", "Pass", "Fail", "Pass", "Pass", "Fail", "Pass", "Pass", "Pass"]
}

df_create = pd.DataFrame(data)
df_create.to_csv("dataset.csv", index=False)

print("CSV file 'dataset.csv' created successfully.\n")

df = pd.read_csv("dataset.csv")

print("First 5 rows:")
print(df.head(), "\n")


print("Last 5 rows:")
print(df.tail(), "\n")

print("Dataset Info:")
print(df.info(), "\n")



print("Summary Statistics:")
print(df.describe(), "\n")

age_column = df["Age"]
print("Selected Single Column (Age):")
print(age_column.head(), "\n")

selected_columns = df[["Age", "Score"]]
print("Selected Multiple Columns (Age, Score):")
print(selected_columns.head(), "\n")

filtered_rows = df[df["Score"] > 80]
print("Filtered rows (Score > 80):")
print(filtered_rows)