import pandas as pd
import numpy as np

df = pd.read_csv(r'Original Data\tb.csv')

df_np = df.to_numpy()

data = [[None, None, None, None, None]]

for row in df_np:
    if(row[5] > 0):
        data.append([row[0], row[1], 'M', "<14", row[5]])
    if(row[6] > 0):
        data.append([row[0], row[1], 'M', "15-24", row[6]])
    if(row[7] > 0):
        data.append([row[0], row[1], 'M', "25-34", row[7]])
    if(row[8] > 0):
        data.append([row[0], row[1], 'M', "35-44", row[8]])
    if(row[9] > 0):
        data.append([row[0], row[1], 'M', "45-54", row[9]])
    if(row[10] > 0):
        data.append([row[0], row[1], 'M', "55-64", row[10]])
    if(row[11] > 0):
        data.append([row[0], row[1], 'M', ">65", row[11]])
    if(row[12] > 0):
        data.append([row[0], row[1], 'M', "nan", row[12]])

    if(row[15] > 0):
        data.append([row[0], row[1], 'F', "<14", row[15]])
    if(row[16] > 0):
        data.append([row[0], row[1], 'F', "15-24", row[16]])
    if(row[17] > 0):
        data.append([row[0], row[1], 'F', "25-34", row[17]])
    if(row[18] > 0):
        data.append([row[0], row[1], 'F', "35-44", row[18]])
    if(row[19] > 0):
        data.append([row[0], row[1], 'F', "45-54", row[19]])
    if(row[20] > 0):
        data.append([row[0], row[1], 'F', "55-64", row[20]])
    if(row[21] > 0):
        data.append([row[0], row[1], 'F', ">65", row[21]])
    if(row[22] > 0):
        data.append([row[0], row[1], 'F', "nan", row[22]])

data = data[1:]
result_df = pd.DataFrame(data, columns=['iso2', 'year', 'sex', 'age', 'count'])
result_df.to_csv(r"Analysis Data\tb.csv")