from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
import math


class CalculadoraScreen(Screen):

    display = StringProperty("0")
    historial = StringProperty("")
    expresion = ""

    def agregar(self, valor):

        if self.display == "0" and valor not in ["+", "-", "*", "/", "."]:
            self.display = valor
            self.expresion = valor
        else:
            self.display += valor
            self.expresion += valor

    def limpiar(self):
        self.display = "0"
        self.expresion = ""
        self.historial = ""

    def borrar(self):

        if len(self.expresion) > 0:
            self.expresion = self.expresion[:-1]

        if self.expresion == "":
            self.display = "0"
        else:
            self.display = self.expresion

    def calcular(self):

        try:
            resultado = eval(self.expresion)

            expresion_visible = self.expresion.replace("*", "×").replace("/", "÷")
            operacion = f"{expresion_visible}= {resultado}"

            self.historial = expresion_visible
            self.display = str(resultado)
            self.expresion = str(resultado)

            self.guardar_historial(operacion)

        except:

            self.display = "Error"
            self.expresion = ""

    def porcentaje(self):

        try:

            resultado = float(self.display) / 100

            self.historial = self.display + "%"

            self.display = str(resultado)
            self.expresion = str(resultado)

        except:
            self.display = "Error"

    def raiz(self):

        try:

            resultado = math.sqrt(float(self.display))

            self.historial = "√(" + self.display + ")"

            self.display = str(resultado)
            self.expresion = str(resultado)

        except:
            self.display = "Error"

    def cuadrado(self):

        try:

            resultado = float(self.display) ** 2

            self.historial = self.display + "²"

            self.display = str(resultado)
            self.expresion = str(resultado)

        except:
            self.display = "Error"

    def inverso(self):

        try:

            resultado = 1 / float(self.display)

            self.historial = "1/(" + self.display + ")"

            self.display = str(resultado)
            self.expresion = str(resultado)

        except:
            self.display = "Error"

    def cambiar_signo(self):

        try:

            numero = float(self.display)

            numero *= -1

            self.display = str(numero)
            self.expresion = str(numero)

        except:
            self.display = "Error"

    def abrir_convertidor(self):
        self.manager.current = "convertidor"

    def guardar_historial(self, operacion):
        import json
        import os

        archivo = "historial.json"

        if os.path.exists(archivo):
            try:
                with open(archivo, "r", encoding="utf-8") as f:
                    datos = json.load(f)
            except:
                datos = []
        else:
            datos = []

        datos.insert(0, operacion)

        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)

    def abrir_historial(self):
        self.manager.current = "historial"