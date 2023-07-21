# C:\Windows\System32\drivers\etc
# open as administrator
file="C:\\Windows\\System32\\drivers\\etc\\hosts"
block="www.codewithharry.com"
unblock="www.codewithharry.com"
ip="127.0.0.1"
check=False

with open(file,"r") as r:
    list=r.readlines()
    for i in list:
        if unblock in i:
            check=True

if check==True:
    with open(file,"r+") as w:
        p=w.read()
        print(p)
        a=p.replace(f"\n{ip} {unblock}","")
        print(a)
    with open(file,"w") as w:
        w.write(f"{a}")



# with open(file,"r") as r:
#     list=r.readlines()
#     for i in list:
#         if block in i:
#             check=True

# if check==False:
#     with open(file,"a") as w:
#         w.write(f"\n{ip} {block}")
#         print("done")



# """
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost
# """