import pandas as pd
import numpy as np


left=pd.DataFrame(
    {'key':['K0','K1','K2','K3'],
     'A':['A0','A1','A2','A3'],
     'B':['B0','B1','B2','B3']
     }
)
right=pd.DataFrame(
    {'key': ['K0', 'K1', 'K2', 'K3'],
     'C': ['C0', 'C1', 'C2', 'C3'],
     'D': ['D0', 'D1', 'D2', 'D3']
     }
)

print(left)
print(right)
# 基于key进行合并
res=pd.merge(left,right,on='key')
print(res)

# consider two keys
left=pd.DataFrame(
    {
     'key1':['K0','K0','K1','K2'],
     'key2':['K0','K1','K0','K1'],
     'A':['A0','A1','A2','A3'],
     'B':['B0','B1','B2','B3']
     }
)
right=pd.DataFrame(
    {
     'key1':['K0','K1','K1','K2'],
     'key2':['K0','K0','K0','K0'],
     'C': ['C0', 'C1', 'C2', 'C3'],
     'D': ['D0', 'D1', 'D2', 'D3']
     }
)
print(left)
print(right)
# how={'left','right','outer','inner'}
# 只考虑相同的key
res=pd.merge(left,right,on=['key1','key2'],how='inner')
print(res)

# 合并后没有对应的用NaN填充
res=pd.merge(left,right,on=['key1','key2'],how='outer')
print(res)

# 以left为基准
res=pd.merge(left,right,on=['key1','key2'],how='left')
print(res)


print('='*50)

# merge中参数 indicator
df1=pd.DataFrame({'coll':[0,1],'col_left':['a','b']})
df2=pd.DataFrame({'coll':[1,2,3],'col_right':[2,2,2]})
print(df1)
print(df2)
# indicator 是显示merge方式 是都有数据还是只有一边有
res=pd.merge(df1,df2,on='coll',how='outer',indicator=True)
print(res)


print('='*50)
# merged bu index
left=pd.DataFrame({
    'A':['A0','A1','A2'],
    'B':['B0','B1','B2']},
    index=['K0','K1','K2']
)
right=pd.DataFrame({
    'C':['C0','C1','C2'],
    'D':['D0','D1','D2']},
    index=['K0','K2','K3']
)
print(left)
print(right)
# left_index and right_index
res=pd.merge(left,right,left_index=True,right_index=True,how='outer')
print(res)

res=pd.merge(left,right,left_index=True,right_index=True,how='inner')
print(res)


print('='*50)
# 实例
boys=pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})
girls=pd.DataFrame({'k':['K0','K0','K3'],'age':[4,5,6]})
# 两个age的名字一样 加后缀
res=pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='inner')
print(res)

res=pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='outer')
print(res)














