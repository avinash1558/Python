import re
import os
print("Email ID tester")
email=input("Email ID :")
vrf=re.search(r"[a-zA-Z0-9]+@gmail.com",email)
print(vrf)
os.system("cls")
if(vrf==None):

    print("Invalid Email ID ")
else:
    print("Valid Email ID ")


# vrf=re.compile(r"[a-zA-Z0-9]+@gmail.com")
# match=vrf.finditer(email)
# # for m in match:
# #     print(m)
