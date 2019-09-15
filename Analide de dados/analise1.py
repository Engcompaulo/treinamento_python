import pandas as pd
import numpy as nu

s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])

print(s)

s = pd.Series([3, -5, 7, 4])

print(s)

data = {
'País': ['Bélgica', 'Índia', 'Brasil'],
'Capital': ['Bruxelas', 'Nova Delhi', 'Brasília'],
'População': [123465, 456789, 987654]
}

df = pd.DataFrame(data, columns=['País','Capital','População'],index=['a', 'b', 'c'])

print(df)

print(sum(df.População))
print(nu.mean(df.População))
print(sum(df.População))
