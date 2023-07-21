n=int(input('Enter n number of apple got by herry potter : '))
mn=int(input('Enter minimum number of apple are divide by n: '))
mx=int(input('Enter maxmum number of apple are divide by n: '))
for i in range(mn,mx+1):
    if n%i==0:
        print(f'{i} is divide by {n}')
    else:
        print(f'{i} is not divide by {n}')