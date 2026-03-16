import pandas as pd

df = pd.read_csv("employee-salary-analysis/data.csv")
print("Dataset:")
print(df)
print("\nAverage Salary Per Department:")
print(df.groupby("department")["salary"].mean())
print("\nHighest Salary")
print(df.sort_values(by = ["salary"], ascending = False).head(1))
print("\nTotal Transaction Per Department:")
print(df.groupby("department")["transaction"].sum())
df["salary_category"] = df["salary"].apply(lambda x : "High" if x >80000 else "Medium" if x >= 60000 else "Low")
print("\n salary_category:")
print(df[["name","salary","salary_category"]])

import matplotlib.pyplot as plt
dept_salary = df.groupby("department")["salary"].mean()

dept_salary.plot(kind="bar", title="Average Salary Per Department")
plt.show()