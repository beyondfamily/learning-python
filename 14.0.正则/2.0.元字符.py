import re

a='张三天天玩游戏，张三@hello玩的，非常开心'
# .的作用查找单个字符，除了换行符，和结束符
res1=re.findall('张三.',a)  # ['张三天', '张三@']
res2=re.findall('张三..',a) # ['张三天天', '张三@h']
res3=re.findall('[三h]',a) # ['三', '三', 'h']

b='<html>000</html><td>ddd</td>'

qiye=re.findall('<.*?>',b) # ['<html>', '</html>', '<td>', '</td>']
qiye=re.findall('<.*>',b) # ['<html>000</html><td>ddd</td>']
url='''
<
imgs class="main_img imgs-hover" 
data-imgurl="https://img1.baidu.com/it/u=2102736929,2417598652&amp;fm=26&amp;fmt=auto" 
src="https://img1.baidu.com/it/u=2102736929,2417598652&amp;fm=26&amp;fmt=auto" 
style="width: 281px; height: 199.451px;"
>
'''
res_1=re.findall('src="(.+?)"',url) # 只会取括号的内容
# ['https://img1.baidu.com/it/u=2102736929,2417598652&amp;fm=26&amp;fmt=auto']

res_2=re.search('src="(.+?)"',url).group() # 获取所有的内容
# src="https://img1.baidu.com/it/u=2102736929,2417598652&amp;fm=26&amp;fmt=auto"

res_3=re.search('"http.*?"',url).group()
# "https://img1.baidu.com/it/u=2102736929,2417598652&amp;fm=26&amp;fmt=auto"

res_4=res_3.replace('"','')
# https://img1.baidu.com/it/u=2102736929,2417598652&amp;fm=26&amp;fmt=auto






