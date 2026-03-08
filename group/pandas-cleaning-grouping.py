import pandas as pd
import numpy as np



data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)
print("\n")


print("Missing Values in Dataset:")
print(df.isnull().sum())
print("\n")


salary_mean = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(salary_mean)

print("Dataset after filling missing Salary values:")
print(df)
print("\n")


df = df.drop(columns=["Temporary_Notes"])

print("Dataset after dropping Temporary_Notes column:")
print(df)
print("\n")



df = df.rename(columns={"Salary": "Annual_Salary"})

print("Dataset after renaming Salary to Annual_Salary:")
print(df)
print("\n")



summary = df.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
)

print("Final Department Summary:")
print(summary)