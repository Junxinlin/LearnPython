#coding:utf-8

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
    "I  had this thing.",
    "you could type up right.",
    "But it didn't sing.",#带有单引号，输出会有双引号区别
    "So I said goodnight."
    )
