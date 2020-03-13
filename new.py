import math
try:
    a = eval(input("请输入a边长:"))
    b = eval(input("请输入b边长: "))
    c = eval(input("请输入c边长: "))
except NameError:
    print("请输入正数数值")
if str.isdigit(a) == True:
    print("输输字")
elif a < 0 or b < 0 or c < 0:
    print("数据不可以为负数")
elif a+b <= c or a+c <= b or b+c <= a:
    print("不符合两边之和大于第三边原则")

else:
    p = (a+b+c)/2
    s = math. sqrt(p * (p-a) * (p-b)*(p-c))
    print("三角形的面积是(:.2f)". format(s))
