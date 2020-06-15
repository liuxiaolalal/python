# a = {'a','a','b','c','c'}
# print(a)
#
# b = set('abcdefcdsa')
# print(b)

# a = {'a','b'}
# b = {'c','d'}
# for x,y in zip(a,b):
#     print(x,y)

# s = "abcdcba123"
# z = s[::-1]
# print(z)
#
# s = "a b c d e f"
# num = len(s.split())
# print(num)

# def judge(s):
#     return s == s[::-1]
# if  __name__ == '__main__':
#     s = input("please enter a str: ")
#     if judge(s):
#         print("yes, it is")
#     else:
#         print("no, it is not")

# def f(a , data = None):
#     if  data == None:
#         data = []
#     data.append(a)
#     return data
# data = f(1)
# print(f(2,data))
# print(f(3))
# print(f(4,data))
#
# a = 123
# c = ["aad",a,"bcd"]
# # print(type(c))
#
# def hello(*,name = 'User'):
#     print("hello",name)
# hello(name='nihao')

# try:
#     # 抛出异常
#     raise ValueError("nihao")
# except ValueError:
#     print("valueError")

import os
print(os.getgid())