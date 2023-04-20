import pandas as pd
import numpy as np
excel_data_df = pd.read_excel('main.xlsx', sheet_name='Sheet1')

# print whole sheet data
print(excel_data_df)


df = pd.DataFrame([[1,'Bob', 'Builder'],
                  [2,'Sally', 'Baker'],
                  [3,'Scott', 'Candle Stick Maker'],
                  [4,'Scott', 'Candle Stick Maker']],
columns=['id','name', 'occupation'])
df.to_excel('main.xlsx')