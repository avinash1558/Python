# iterable =>__iter__() and __getitem()
# iterator => __next__()
# iteration=> 

def gen(n):
    for i in range(n):
        yield i

avi=gen(23)
print(avi.__next__())
print(avi.__next__())
print(avi.__next__())

a='avinash'
g=iter(a)
print(g.__next__())