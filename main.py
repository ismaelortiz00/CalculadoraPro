from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.floatlayout import FloatLayout

from screens.calculadora import CalculadoraScreen
from screens.convertidor import ConvertidorScreen
from screens.historial import HistorialScreen


class CalculadoraProApp(App):
    def build(self):
        Builder.load_file("calculadora.kv")

        root = FloatLayout()

        sm = ScreenManager(size_hint=(1, 1), pos_hint={"x": 0, "y": 0})
        sm.add_widget(CalculadoraScreen(name="calculadora"))
        sm.add_widget(ConvertidorScreen(name="convertidor"))
        sm.add_widget(HistorialScreen(name="historial"))

        root.add_widget(sm)

        return root


if __name__ == "__main__":
    CalculadoraProApp().run()