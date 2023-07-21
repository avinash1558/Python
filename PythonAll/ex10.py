import pickle
with open('txt.txt') as p:
    data=p.read().split('\n')
    data1=[i.split(',') for i in data ]
    # print(data1)
with open('pikl.pkl','wb') as p:
    pickle.dump(data1,p)
with open('pikl.pkl','rb') as p:
    print(pickle.load(p))

