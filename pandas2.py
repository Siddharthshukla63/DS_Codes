import pandas as pd
score = pd.DataFrame({'subject': ['Math', 'Science', 'English', 'History'],
                      'score': [85, 90, 78, 88]})
avg =score.groupby('subject')['score'].mean()
print(avg)