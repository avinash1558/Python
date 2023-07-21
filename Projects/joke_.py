# pip install pyjokes
import pyjokes

MyJoke = pyjokes.get_joke(language="hi", category="all")
print(MyJoke)