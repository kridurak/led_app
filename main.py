import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import client as cl

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # Set collumns
        self.cols = 1

        self.header = Label(
            text="LED osvetlenie",
            font_size=38
        )
        self.add_widget(self.header)

        self.state = "off"
        self.label = Label(
            text="Stav",
            font_size=38
        ) 
        self.add_widget(self.label)

        # Create a Submit Button
        self.off = Button(
            text="ON", 
            font_size=32,
        )
        self.off.bind(on_press = self.pressOn)
        self.add_widget(self.off)
        
        self.on = Button(
            text="OFF", 
            font_size=32
        )
        self.on.bind(on_press = self.pressOff)
        self.add_widget(self.on)
    
    def pressOn(self, instance):
        self.state = "on"
        cl.setState("off")
        self.label.text = "Zapnuté"
    
    def pressOff(self, instance):
        self.state = "off"
        cl.setState("on")
        self.label.text = "Vypnuté"

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()