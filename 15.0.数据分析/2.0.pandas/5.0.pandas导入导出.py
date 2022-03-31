import numpy as np
import pandas as pd

# 读取csv文件
data=pd.read_csv('Database/student.csv')
print(data)

# 以pickle类型导出
data.to_pickle('Database/student.pickle')





