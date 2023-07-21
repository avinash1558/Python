from googletrans import Translator
t=Translator()
p=t.translate("i am avinash",dest="hi")
print(p)
# pip install googletrans==4.0.0rc1