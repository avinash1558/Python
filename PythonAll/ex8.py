import os
def filRename(path,filePath,format):
    os.chdir(path)
    i=1
    files = os.listdir(path)
    with open(filePath,'r') as p:
        fileList = p.read().split("\n")
        data = [f.capitalize() for f in fileList]
    with open(filePath, 'w') as p:
        for f in data:
            p.write(f + '\n')
    for file in files:
        if os.path.splitext(file)[1] != format:
            os.renames(file,f"{i*10}{format}")
            i+=1

filRename(r"C:\Users\HP\Desktop\delete",r"C:\pycode\python\name.txt",'.png')