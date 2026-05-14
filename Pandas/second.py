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
