import pandas as pd
import numpy as np

dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan
print(df)

# 有任何一个NaN 就丢掉一整行
# how={'any','all'} 只有所有都为NaN是才会丢掉行或者列
print(df.dropna(axis=0,how='any'))

# 填上NaN的数据
print(df.fillna(value=0))

# 检测是否有缺失数据
print(df.isnull())

# 寻找是否至少有一个True
print(np.any(df.isnull()==True))









