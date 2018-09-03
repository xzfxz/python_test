#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
import sys,getopt

'''
打印脚本的名称，以及该脚本的参数
sys.argv 数组包含 文件名在内的所有参数列表，其中0是脚本文件名称，其他参数从1开始
'''
print("ScriptName: ", sys.argv[0])
for i in range(1, len(sys.argv)):
    print("args", i, sys.argv[i])


'''

使用getopt获取方法，脚本参数

'''
opts, args = getopt.getopt(sys.argv[1:], "hi:p:",["help","ip=",'port='])
'''
    getopt（）方法的 
    第一个参数：脚本的所有参数 ，
    第二个参数 短参数，其中h后面没有：表示该参数后面没有参数值，
    第三个参数 长参数 help后面没有等号=，表示后面不带参数，其他三个有=，表示后面需要参数
    返回结果，第一个options 包含元组的列表，[('-i','127.0.0.1'),('-p','80')]
    第二个参数args 包含那些没有‘-’或‘--’的参数
'''
print(opts)
print("***")
print(args)
ip=""
port=""
for op, value in opts:
    if op == "-i":
        ip = value
    elif op == "-p":
        port = value
    elif op == "-h":
        print('this is a help 2 this script')
        sys.exit()
print("ip{}".format(ip))
print("port{}".format(port))
