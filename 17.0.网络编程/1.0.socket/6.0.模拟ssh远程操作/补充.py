import os
import subprocess
# 执行系统命令

# res=os.system('ipconfig')
print('='*80)


res=subprocess.Popen('ipconfig',shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     )

# 从正确的管道中读取
print(res.stdout.read().decode('gbk'))





