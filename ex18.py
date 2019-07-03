# -*- coding:utf-8 -*-
def print_two(*args):
    arg1,arg2 = args
    print "arg1: %r, arg2: %r" % (arg1,arg2)


def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1,arg2)


def print_one(arg1):
    print "arg1: %r" % arg1


def print_none():
    print "I got nothing."


def test():
    print "Why?"

#调用
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
test()
print_none()
