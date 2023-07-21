import re
data='avinash sharma is good 122-111 omg and is ae aame '
p=re.compile(r"avi")
# p=re.compile(r".i")
# p=re.compile(r"good$")
# p=re.compile(r"^avi")
# p=re.compile(r"o*")
# p=re.compile(r"o+")
# p=re.compile(r"o{2}")
# p=re.compile(r"\d{3}-\d{3}")
p=re.compile(r"\bavi")
mat=p.finditer(data)
for m in mat:
    print(m)