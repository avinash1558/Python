import json
data1 ='{"a":"v","123":"112","is":"12"}'
print(type(data1))
parsed1 = json.loads(data1)
print(type(parsed1))
data1 ="""{"a":"v","123":"112","is":"12"}"""
parsed1 = json.loads(data1)
print(parsed1)

with open('avi.json','r') as f:
    data1 = json.load(f)
    print(type(data1))
    p=f.read()
    print(type(p))
    print(data1)


# f=["avinash","avinash","avinash"]   
# data =[ i.capitalize() for i in f]
# print(data[2])

data2 ={"a":"v","123":112,"a":False,"is":"12"}
print(type(data2))
parsed2 = json.dumps(data2)
print(parsed2)
print(type(parsed2))
