import pandas as pd
import numpy as np

print("=" * 60)
print("PANDAS BASIC TUTORIAL")
print("=" * 60)

# Create DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['NYC', 'LA', 'Chicago', 'Boston'],
    'Salary': [70000, 80000, 90000, 75000]
}
df = pd.DataFrame(data)

print("\n1. CREATE DATAFRAME")
print(df)

print("\n2. BASIC INSPECTION")
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"Data types:\n{df.dtypes}")

print("\n3. VIEW DATA")
print("First 2 rows:\n", df.head(2))
print("Last 2 rows:\n", df.tail(2))

print("\n4. SELECTION & INDEXING")
print("Select column 'Name':\n", df['Name'])
print("Select rows by position:\n", df.iloc[0:2])
print("Select by label:\n", df.loc[0:1, ['Name', 'Age']])

print("\n5. FILTERING")
print("Age > 28:\n", df[df['Age'] > 28])
print("Name starts with 'A':\n", df[df['Name'].str.startswith('A')])

print("\n6. SORTING")
print("Sort by Age (descending):\n", df.sort_values('Age', ascending=False))

print("\n7. ADDING COLUMNS")
df['Bonus'] = df['Salary'] * 0.1
df['Annual_Total'] = df['Salary'] + df['Bonus']
print(df)

print("\n8. MISSING DATA")
df_missing = pd.DataFrame({'A': [1, np.nan, 3], 'B': [np.nan, 5, 6]})
print("DataFrame with NaN:\n", df_missing)
print("Fill NaN with 0:\n", df_missing.fillna(0))

print("\n9. GROUPBY")
grouped = df.groupby('City')['Salary'].mean()
print("Average Salary by City:\n", grouped)

print("\n10. AGGREGATION")
print("Statistics:\n", df.describe())
print("Mean Age:", df['Age'].mean())
print("Max Salary:", df['Salary'].max())

print("\n11. MERGE DATAFRAMES")
df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
df2 = pd.DataFrame({'ID': [1, 2], 'Dept': ['IT', 'HR']})
merged = pd.merge(df1, df2, on='ID')
print("Merged DataFrame:\n", merged)

print("\n12. DATETIME")
df['Join_Date'] = pd.to_datetime(['2023-01-15', '2022-03-20', '2021-07-01', '2023-06-10'])
df['Year'] = df['Join_Date'].dt.year
print(df[['Name', 'Join_Date', 'Year']])

print("\n13. EXPORT")
df.to_csv('output.csv', index=False)
print("Saved to output.csv")

print("\n14. SERIES BASICS")
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("Series:\n", s)
print("Series mean:", s.mean())
print("Series cumulative sum:\n", s.cumsum())

print("\n15. PIVOT TABLE")
pivot = df.pivot_table(values='Salary', index='City', aggfunc='mean')
print("Pivot Table:\n", pivot)

print("\n" + "=" * 60)
print("TUTORIAL COMPLETE")
print("=" * 60)