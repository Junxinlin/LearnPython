#coding:utf-8

#把字符串赋给一个变量
x = "There are %d types of people." % 10
#把binary赋给binary
binary = "binary"
#把don't赋给do_not
do_not = "don't"
#把前两个变量嵌入字符串中，并重新赋值一个变量
y = "Those who know %s and those who %s." % (binary,do_not)

#输出x,y
print x
print y

#在输出语句中使用格式化字符
print "I said: %r." % x
print "I also said: '%s'." % y

#变量嵌套
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

#变量合并
w = "This is the left side of..."
e = "a string with a right side."

print w + e
