# write
# p=open("file_reading.txt","w")
# str1= "are all good"
# print(p.write(str1))#length of word

# appending
# p=open("file_reading.txt","a")
# str1= "are all good\n"
# p.write(str1)
# p.write(str1)
# p.write(str1)

# write and read
p=open("file_reading.txt","r+")
print(p.read())
str1= "are all good"
print(p.write(str1))#length of word
