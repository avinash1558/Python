# map
# l=[12,111,2,3,321,1,23232]
# a=list(map(str,l))
# print(a)
# c=list(map(int,a))
# print(c)

# l=[6,1,2,3,3,1,2]
# a=list(map(lambda a:a*a, l))
# print(a)
# def fun(a):
#     return a+a
# def fun1(a):
#     return a*a
# fan=[fun,fun1]
# for i in range(6):
#     c=list(map(lambda x:x(i),fan))
#     print(c)

# filter
l=[12,11,33,45,6,12,34,53,3]
# def fan(a):
#     return a<=33
# l1=list(filter(fan, l))
l1=list(filter(lambda a:a<=33, l))
print(l1)

# reduce
import functools 
l=[12,11,33,45,70,12,34,53,3]
a=functools.reduce(lambda a,s:a+s,l)
print(a)