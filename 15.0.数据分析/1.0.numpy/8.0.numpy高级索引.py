import numpy as np

# 如果一个ndarray是非元组序列，数据类型为整数或布尔值的ndarray，或者至少一个元素为序列对象的元组，我们就能够用它来索引ndarray。高级索引始终返回数据的副本。 与此相反，切片只提供了一个视图。
# 有两种类型的高级索引：整数和布尔值。

# 整数索引
# 该结果包括数组中(0,0)，(1,1)和(2,0)位置处的元素。
x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0, 1, 2], [0, 1, 0]]
print(y)

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print(y)

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
# 切片
z = x[1:4,1:3]
print(z)
# 对列使用高级索引
y = x[1:4,[1,2]]
print(y)

print('='*80)
# 布尔索引
# 当结果对象是布尔运算（例如比较运算符）的结果时，将使用此类型的高级索引。
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print(x)
print('大于 5 的元素是：')
print(x[x>5])
print(x[x%2==0])

# 这个例子使用了~（取补运算符）来过滤NaN。
a = np.array([np.nan,  1,2,np.nan,3,4,5])
print(a)
print(a[~np.isnan(a)])

# 以下示例显示如何从数组中过滤掉非复数元素。
a = np.array([1,  2+6j,  5,  3.5+5j])
print(a[np.iscomplex(a)])
















