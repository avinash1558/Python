import pickle
a=['avinash',123,'sharma',1222]
file="mycar.pkl"
f=open(file,'wb')
pickle.dump(a,f)
f.close()

a=['avinash',123,'sharma',1222]
file="mycar.pkl"
f=open(file,'rb')
m=pickle.load(f)
print(m)
f.close()