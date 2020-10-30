from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.inside = GridLayout() # cria um novo layout
        self.inside.cols = 2 # novo grid layout com 2 colunas

        self.inside.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside) # adiciona o layout interno
        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed) # vincula o evento
        self.add_widget(self.submit) # adiciona o bot�o ao layout principal


    def pressed(self, instance): # implementa��o do evento
        name = self.name.text
        last = self.lastName.text
        email = self.email.text

        print("Name:", name, "Last Name:", last, "Email:", email)

        self.name.text = ""
        self.lastName.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
