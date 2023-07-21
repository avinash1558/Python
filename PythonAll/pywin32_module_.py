# pip install pywin32
# attribute error is come when module and file name is same
# def speak(str):
#     from win32com.client import Dispatch
#     speak=Dispatch('SAPI.SpVoice')
#     speak.Speak(str)
# speak('avinash sharmaa')
from win32com.client import Dispatch
Dispatch('SAPI.SpVoice').Speak('avinasj ahajs')