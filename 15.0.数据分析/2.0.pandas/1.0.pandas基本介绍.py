import numpy as np
import pandas as pd


s=pd.Series([1,3,6,np.nan,44,1])
print(s)

# 时间方面
dates=pd.date_range('20160101',periods=6)
print(dates)

# 创建一个二位的数据
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)

df1=pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)

df2=pd.DataFrame({
    'A':1,
    'B':pd.Timestamp('20130102'),
    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
    'D':np.array([3]*4,dtype='int32'),
    'E':pd.Categorical(['test','train','test','train']),
    'F':'foo'
})
print(df2)
print(df2.dtypes)
# 输出所有列的标序
print(df2.index)
# 输出所有行的标序
print(df2.columns)
# 输出具体的值
print(df2.values)
# 统计数字类型数据的部分数据
print(df2.describe())
# 矩阵的转质
print(df2.T)
# 排序
print(df2.sort_index(axis=1,ascending=False))
print(df2.sort_index(axis=0,ascending=False))
# 根据数据里面的具体排序
print(df2.sort_values(by='E'))

















