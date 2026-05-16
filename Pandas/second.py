import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}   
df = pd.DataFrame(data)         
print(df)       


data.tail(2)

data.head(2)

data.values_counts()

data.describe()

data.info()

data['Age'].mean()

data['Age'].median()

data['Age'].mode()

data['Age'].std()

data['Age'].min()

data['Age'].max()

data['Age'].quantile(0.25)

data['Age'].quantile(0.75)

data.copy()
