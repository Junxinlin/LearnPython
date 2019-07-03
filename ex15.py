#coding:utf-8

#导入模组
from sys import argv

#解包
script, filename = argv

#调用open函数，获取文件赋给变量
txt = open(filename)

#打印
print "Here's your file %r:" % filename
#读取文件内容
print txt.read()
txt.close()

#使用raw_input再次调用文件
print "Type the filename again:"
file_again = raw_input('>')

txt_again = open(file_again)

#打印文件内容
print txt_again.read()

txt_again.close()

