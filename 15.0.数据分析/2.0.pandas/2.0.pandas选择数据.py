import pandas as pd
import numpy as np

dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df)
# 获取A列数据
print(df['A'],df.A)
# 获取多行
print(df[0:3],df['20130102':'20130104'])

# 以具体标签的名称来选择
# 输出一行
print(df.loc['20130102'])
# 输出多列
print(df.loc[:,['A','B']])
# 指定的部分数据
print(df.loc['20130102',['A','B']])

# 以具体标签的位置来选择
print(df.iloc[3:5,1:3])
print(df.iloc[[1,3,5],1:3])

# 布尔筛选
print(df[df.A>8])








