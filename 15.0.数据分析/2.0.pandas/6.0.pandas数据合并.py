import numpy as np
import pandas as pd

df1=pd.DataFrame(np.ones((3,4))*0,columns=['A','B','C','D'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['A','B','C','D'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['A','B','C','D'])


# 数据的合并concat()
res=pd.concat([df1,df2,df3],axis=0)
print(res)
# 重新定义index
res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(res)


# join,['inner','outer']
df1=pd.DataFrame(np.ones((3,4))*0,columns=['A','B','C','D'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['B','C','D','E'],index=[2,3,4])
print(df1)
print(df2)
res=pd.concat([df1,df2],join='outer') # outer保留
print(res)
res=pd.concat([df1,df2],join='inner',ignore_index=True) # inner舍去
print(res)


print('='*50)
# append
df1=pd.DataFrame(np.ones((3,4))*0,columns=['A','B','C','D'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['A','B','C','D'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['B','C','D','E'],index=[2,3,4])
res=df1.append(df2,ignore_index=True)
res=df1.append([df2,df3])
print(res)

s1=pd.Series([1,2,3,4],index=['A','B','C','D'])
res=df1.append(s1,ignore_index=True)

print(res)


