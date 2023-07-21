# pip install pywhatkit
# pip install flask

import pywhatkit
text="""avimasj ajska dkjILAMD
isjlsd sdskdn dasndjnsjlnkdnsjndjnsa AS F"""

# pw.text_to_handwriting(text,file,[color rgb])
pywhatkit.text_to_handwriting(text,"d.png",[0,0,138])
print("done")