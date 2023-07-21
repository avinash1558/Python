def matchingWord(s1,s2):
    w1=s1.split(' ')
    w2=s2.split(' ')
    score=0
    for w in w1:
        for b in w2:
            if w.lower()==b.lower():
                score +=1
    return score
sentences=['python is good lenguage','this is python code is compile by python',  'avinash is good coder']
search=input('Please enter string : \n')
scores=[matchingWord(search,sentence) for sentence in sentences]
sortScore=[Score for Score in sorted(zip(scores,sentences),reverse=True)]
zeroScore=0
for s in scores:
    if s==0:
        zeroScore+=1 
print(f"{len(sortScore)-zeroScore} result found!!")
for score , item in sortScore:
    if score>0:
        print(f"\"{item}\"")