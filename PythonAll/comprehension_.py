# l1=[]
# for i in range(20):
#     if i%3==0:
#         l1.append(i)
# print(l1)

# l2=[i for i in range(20) if i%3==0]
# print(l2)

# dicts={ f'item {i+1}':i+1 for i in range(10)}
# print(dicts)

gen=(i for i in range(20)if i%3==0)
print(gen)
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
