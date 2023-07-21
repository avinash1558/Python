
from kivy.app import App
import os
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout


class Stack_Layout(StackLayout):
    pass
# class Grid_Layout(GridLayout):
#     pass
class Anchor_Layout(AnchorLayout):
    pass
class Box_Layout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(6):
            a=Button(text=str(i+1),size_hint=(None,None));
            self.add_widget(a)
    """    Button:
        text:"B"
        size_hint:0.3,0.2
    Button:
        text:"B"
        size_hint:0.3,0.2
    Button:
        text:"B"
        size_hint:0.3,0.2
    Button:
        text:"B"
        size_hint:0.3,0.2
    Button:
        text:"B"
        size_hint:0.3,0.2
    Button:
        text:"B"
        size_hint:0.3,0.2
    Button:
        text:"B"
        size_hint:0.3,0.2"""
    pass
class MainWidget(Widget):
    pass

class FirstApp(App):
    pass
FirstApp().run()
os.system("cls")