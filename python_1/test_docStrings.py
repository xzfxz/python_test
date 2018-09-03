def print_max(a,b):
    '''
    打印两个参数的最大值，保证这两个数必须是数值类型
    :param a:第一个参数
    :param b:第二个参数
    :return:返回值
    '''
    x = int(a)
    y= int(b)
    if(x > y):
        print(x,"is max")
    else:
        print(y,"is max")

print_max(4,5)
print(print_max.__doc__)
