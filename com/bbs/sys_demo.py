import sys

'''
sys 包api:
argv : 获取命令行参数，第一个参数为启动py文件路径，后续为输入命令行参数
'''
args = sys.argv
print(len(args), type(args), args)
