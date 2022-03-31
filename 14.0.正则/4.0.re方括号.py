# []代表的是一个字符位置上的数是某个范围或是某个
import re

part1 = re.compile('[abc]')
part2 = re.compile('[abc]monkey')
part3 = re.compile('[^abc]monkey')

str = 'this amonkey is a 1 bmonkey this cmonkey is a  c wmonkey'

res_1 = re.findall(part1, str)  # ['a', 'a', 'b', 'c', 'a', 'c']
res_2 = re.findall(part2, str)  # ['amonkey', 'bmonkey', 'cmonkey']
res_3 = re.findall(part3, str)  # ['wmonkey']

part1 = re.compile('[1-9]monkey')
str='this a2monkey is a 1 b4monkey this c9monkey is a  c wmonkey'
res_1=re.findall(part1,str) # ['2monkey', '4monkey', '9monkey']

part1=re.compile('[125-8]monkey')
str='this 128monkey is a 1 126monkey this 455c9monkey is a  c wmonkey this 1monkey is a  c 2monkey'
res_1=re.findall(part1,str) # ['8monkey', '6monkey', '1monkey', '2monkey']




