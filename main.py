import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    #Initialize infinite keywords
    def __init__(self):
        pass

class MyApp(App):
    def build(self):
        return Label(text = 'Hello World')
    
if __name__ == '__main__':
    MyApp().run()