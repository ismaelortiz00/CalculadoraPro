from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty
from kivy.uix.button import Button
import json
import os

HISTORIAL_FILE = "historial.json"


class HistorialScreen(Screen):
    items = ListProperty([])
    titulo = StringProperty("Historial")
    seleccion = StringProperty("")

    def on_pre_enter(self):
        self.cargar()
        self.mostrar()

    def cargar(self):
        if os.path.exists(HISTORIAL_FILE):
            try:
                with open(HISTORIAL_FILE, "r", encoding="utf-8") as f:
                    self.items = json.load(f)
            except:
                self.items = []
        else:
            self.items = []

    def guardar(self):
        with open(HISTORIAL_FILE, "w", encoding="utf-8") as f:
            json.dump(self.items, f, ensure_ascii=False, indent=2)

    def mostrar(self):
        lista = self.ids.lista_historial
        lista.clear_widgets()

        if not self.items:
            btn = Button(
                text="Sin historial",
                size_hint_y=None,
                height=80,
                background_color=(0, 0, 0, 0),
                color=(0.7, 0.7, 0.7, 1),
                font_size=22
            )
            lista.add_widget(btn)
            return

        for item in self.items:
            btn = Button(
                text=item,
                size_hint_y=None,
                height=70,
                background_color=(0, 0, 0, 0),
                color=(0.9, 0.9, 0.9, 1),
                font_size=22,
                halign="right",
                valign="middle"
            )
            btn.text_size = (330, None)
            btn.bind(on_press=lambda btn: self.seleccionar(btn.text))
            lista.add_widget(btn)

    def seleccionar(self, texto):
        self.seleccion = texto
        self.titulo = "1 elemento seleccionado"

    def volver(self):
        self.titulo = "Historial"
        self.seleccion = ""
        self.manager.current = "calculadora"

    def recalcular(self):
        if self.seleccion:
            calc = self.manager.get_screen("calculadora")
            expresion = self.seleccion.split("=")[0].strip()
            expresion = expresion.replace("×", "*").replace("÷", "/")
            calc.expresion = expresion
            calc.display = expresion
            self.manager.current = "calculadora"

    def eliminar_uno(self):
        if self.seleccion in self.items:
            self.items.remove(self.seleccion)
            self.guardar()
            self.seleccion = ""
            self.titulo = "Historial"
            self.mostrar()

    def eliminar_todo(self):
        self.items = []
        self.guardar()
        self.seleccion = ""
        self.titulo = "Historial"
        self.mostrar()