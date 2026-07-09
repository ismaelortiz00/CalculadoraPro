from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from screens.calculadora import CalculadoraScreen
from screens.convertidor import ConvertidorScreen
from screens.historial import HistorialScreen


class CalculadoraProApp(App):
    def build(self):
        Builder.load_file("calculadora.kv")

        sm = ScreenManager()
        sm.add_widget(CalculadoraScreen(name="calculadora"))
        sm.add_widget(ConvertidorScreen(name="convertidor"))
        sm.add_widget(HistorialScreen(name="historial"))

        return sm


if __name__ == "__main__":
    CalculadoraProApp().run()