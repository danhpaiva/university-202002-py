from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label


class Tela(GridLayout):
    def __init__(self, **kwargs):
        super(Tela, self).__init__(**kwargs)
        self.cols = 1

        # slider vertical
        self.sl = Slider(orientation='vertical', min=0, max=100, value=50)
        self.add_widget(self.sl)

        # barra de progresso
        self.pb = ProgressBar(max=100)
        self.pb.value = 50
        self.add_widget(self.pb)

        # exibir texto simples
        self.add_widget(Label(text='Valor Atual :'))

        # valor do slider
        self.valor = Label(text='0')
        self.add_widget(self.valor)

        # vinculando evento ao slider
        self.sl.bind(value=self.on_value)

    def on_value(self, instance, valor):
        self.valor.text = "%d" % valor
        self.pb.value = valor



class MyApp(App):
    def build(self):
        return Tela()

if __name__ == '__main__':
    MyApp().run()
