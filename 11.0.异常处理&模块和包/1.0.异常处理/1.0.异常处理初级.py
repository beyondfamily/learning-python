'''
异常分为两种
  1.语法错误导致的异常
  2.逻辑错误导致的异常

如果错误发生的原理不可预知，就可以使用try。。。except。。。 在错误发生的时候进行处理

try:
    可能发生什么错误的代码
except:
    如果发生异常则进入 except 代码块进行处理
'''
# 假设读取的文件不存在，会发生错误，可以使用两种方式进行处理
# 1.可以在文件读取前先判断当前文件是否存在
# 2.也可以使用try
# 注意try。。。except。。。是在错误发生后进行的处理
try:
    with open('./uesr.txt','r') as fp:
        res=fp.read()
    print(res)
except:
    print('文件不存在')
print('程序的继续执行...')

print('='*80)

# 1.使用try..except... 处理指定的异常类，如果引发了非指定的异常，则无法处理
try:
    s1='hello'
    int(s1)  # 会引发ValueError
except ValueError as e:
# except IndexError as e: # 如果引发了非指定的异常，则无法处理
    print(e)

print('='*80)

# 2.多分支处理异常类
s1='hello'
try:
    # int(s1) # ValueError
    s1[5] # IndexError
except IndexError as e:
     print('IndexError',e)
except KeyError as e:
     print('KeyError',e)
except ValueError as e:
     print('ValueError',e)

print('='*80)

# 3.通用异常类 Exception
s1='world'
try:
    int(s1)
except Exception as e:
    print(e)

print('='*80)

# 4.多分支异常类+通用异常类
s1='hello'
try:
    # int(s1) # ValueError
    s1[5] # IndexError
except IndexError as e:
     print('IndexError',e)
except KeyError as e:
     print('KeyError',e)
except ValueError as e:
     print('ValueError',e)
except Exception as e:
    print('Exception',e)

print('='*80)

# 5.try...except...else...finally
# finally 无论是否引发异常 都会执行 通常情况下用于执行一些清理工作
s1='hello'
try:
    int(s1)
    print('如果前面的代码引发了异常，这个代码将不在继续执行...')
except IndexError as e:
    print('IndexError',e)
except KeyError as e:
     print('KeyError',e)
except ValueError as e:
     print('ValueError',e)
else:
    print('try代码块中没有引发异常是，执行')
finally:
    print('无论是否引发了异常都会执行这个代码')

print('='*80)

# 6.使用raise 判断预计，主动抛出异常
try:
    # 可以使用raise主动抛出异常 并设置异常参数
    raise Exception('发生错误')
except Exception as e:
    print('Exception',e)

print('='*80)

# 7.assert 断言
try:
    assert 2==1 # 不成立 断言错误 AssertionError 若成立则无事发生
except Exception as e:
    print('断言错误')



