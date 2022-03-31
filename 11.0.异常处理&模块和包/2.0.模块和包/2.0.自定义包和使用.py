# 如果需要使用包可以直接导入包
import Package  # 同级内容
# 1.直接把包当做模块导入，可以用的内容是__init__.py文件中定义的
# 不推荐这种方法
Package.funcpa()

# 2.可以导入模块中的所有内容：注意这个内容是由 __init__.py文件中定义的__all__ 这个变量指定的
# 好处是可以直接导入指定对象的所以模块，并且使用时，直接使用指定的模块名即可
from Package import *
a.funca()
b.funcb()

# 3. 导入指定包中的指定模块
from Package import a,b
a.funca()
b.funcb()

# 4.从指定包的指定模块中导入指定的内容
from Package.b import funcb
funcb()

# 5.从指定包的子包中导入模块
from Package.ps import c
c.funcc()

# 6. 从指定包的子包的指定模块中导入指定内容
from Package.ps.d import funcd
funcd()


# 导入方式得分类 绝对导入


