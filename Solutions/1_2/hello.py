print('hello world')
print('胡','煜','环')

"""
结果:
hello world
胡 煜 环 这里有空格
"""

name = input('你的名字是:')
print('我的名字是', name, sep='') #如果要删除 print() 输出的字符中间的空格，增加 sep=''
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

# 输出 Python 的每个字母
for letter in name:
   if letter == 'h':
      pass
      print('这是 pass 块')
   print('当前字母 :', letter)
 
print("Good bye!")
