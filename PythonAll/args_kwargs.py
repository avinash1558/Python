# def function(*a):
#     for i in a:
#         print(f"it is *args {i}")
# l=[12,13,321,123,112,3333,111]
# function(*l)

# def function(n,a):
#     print(n)
#     for i in a:
#         print(f"it is *args {i}")
# my=123456789009877654321
# l=[12,13,321,123,112,3333,111]
# function(my,l)

def function(n,*a,**k):
    print(n)
    print(type(a),type(k))
    for i in a:
        print(f"it is *args {i}")
    for i,k in k.items():
        print(f"it is *args {i} and {k}")
my=123456789009877654321
l=[12,13,321,123,112,3333,111]
print(l)
p={'avinash':'sharma','age':18,'15':12}
function(my,*l,**p)
print(l)