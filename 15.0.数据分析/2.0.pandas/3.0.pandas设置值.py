import pandas as pd
import numpy as np


dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df)
df.iloc[2,2]=1111
df.loc['20130101','B']=2222
print(df)
# 对A这一列大于10的所在行都变成0
df[df.A>10]=0
print(df)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
# 对A列中具体的数据进行改变
df.B[df.A>10]=0
print(df)
print('='*50)
# 新添加
df['F']=np.nan
df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101',periods=6))
print(df)









