import pandas as pd



data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah"],
    "Score": [95, 88, 72, 91, 67, 85, 93, 78],
    "Passed": [True, True, False, True, False, True, True, False],
    "Category": ["A", "B", "C", "A", "C", "B", "A", "B"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)
print("\n")


print("Single Column Selection (Score):")
score_column = df["Score"]
print(score_column)
print("\n")



print("Multiple Column Selection (Name, Score):")
selected_df = df[["Name", "Score"]]
print(selected_df)
print("\n")



print("First three rows using iloc:")
first_three = df.iloc[:3]
print(first_three)
print("\n")



df_indexed = df.set_index("Name")

print("Accessing row using loc (index = 'Alice'):")
print(df_indexed.loc["Alice"])
print("\n")



high_scores = df[df["Score"] > 85]

print("Students with Score > 85:")
print(high_scores)
print("\n")



high_passed = df[(df["Score"] > 85) & (df["Passed"] == True)]

print("Students with Score > 85 AND Passed = True:")
print(high_passed)
print("\n")



sorted_high_passed = high_passed.sort_values(by="Score", ascending=False)

print("High-performing students sorted by Score (descending):")
print(sorted_high_passed[["Name", "Score"]])
print("\n")



print("Chained filtering + sorting (Score > 85 and Passed=True):")
chained_result = df[(df["Score"] > 85) & (df["Passed"])].sort_values(by="Score", ascending=False)

print(chained_result[["Name", "Score"]])