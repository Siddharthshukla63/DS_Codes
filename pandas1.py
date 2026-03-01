import pandas as pd 
data = {'name': ['alice', 'siddharth', 'john', 'mike'],
        'age': [24, 27, 22, 32],
        'city': ['lucknow', 'delhi', 'mumbai', 'bangalore']}
df = pd.DataFrame(data)
print(df)