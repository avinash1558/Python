# l=['a','s','d','f','g','h']
# p=1
# for i in l:
#     if p%2 != 0:
#         print(f'it is alpa {i}')
#     p+=1
# enumerate
l=['a','s','d','f','g','h']
for i ,p in enumerate(l):
    if i%2 != 0:
        print(f'it is alpa {p}')