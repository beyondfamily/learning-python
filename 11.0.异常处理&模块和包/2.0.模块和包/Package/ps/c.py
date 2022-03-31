def funcc():
    print('funcc')

# 假设在这个模块中如果需要 当前包中的d模块
from . import d
d.funcd()

from .d import funcd
funcd()

# 可以在这个模块中去使用上一级中的模块
from ..import a
a.funca()

from ..b import funcb
funcb()


# 间接应用不能直接在一个文件执行

