from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

from converters import longitud, masa, temperatura, tiempo, area, volumen, datos, velocidad, divisas, sistema
from converters import descuento, finanzas, imc


class ConvertidorScreen(Screen):

    def volver(self):
        self.manager.current = "calculadora"

    def abrir_popup(self, titulo, unidades, funcion):
        layout = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )

        entrada = TextInput(
            hint_text="Ingrese valor",
            multiline=False,
            input_filter="float",
            font_size=22
        )

        origen = Spinner(
            text=unidades[0],
            values=unidades,
            font_size=18
        )

        destino = Spinner(
            text=unidades[1] if len(unidades) > 1 else unidades[0],
            values=unidades,
            font_size=18
        )

        resultado = Label(
            text="Resultado",
            font_size=22
        )

        boton = Button(
            text="Convertir",
            font_size=20,
            background_color=(1, 0.45, 0.05, 1)
        )

        def calcular(_):
            try:
                r = funcion(entrada.text, origen.text, destino.text)
                resultado.text = f"{entrada.text} {origen.text} = {r} {destino.text}"
            except Exception:
                resultado.text = "Valor inválido"

        boton.bind(on_press=calcular)

        layout.add_widget(Label(text=titulo, font_size=24, bold=True))
        layout.add_widget(entrada)
        layout.add_widget(origen)
        layout.add_widget(destino)
        layout.add_widget(boton)
        layout.add_widget(resultado)

        popup = Popup(
            title=titulo,
            content=layout,
            size_hint=(0.9, 0.75)
        )
        popup.open()

    def abrir_longitud(self):
        self.abrir_popup("Longitud", list(longitud.UNIDADES.keys()), longitud.convertir)

    def abrir_masa(self):
        self.abrir_popup("Masa", list(masa.UNIDADES.keys()), masa.convertir)

    def abrir_temperatura(self):
        self.abrir_popup("Temperatura", ["C", "F", "K"], temperatura.convertir)

    def abrir_tiempo(self):
        self.abrir_popup("Tiempo", list(tiempo.UNIDADES.keys()), tiempo.convertir)

    def abrir_area(self):
        self.abrir_popup("Área", list(area.UNIDADES.keys()), area.convertir)

    def abrir_volumen(self):
        self.abrir_popup("Volumen", list(volumen.UNIDADES.keys()), volumen.convertir)

    def abrir_velocidad(self):
        self.abrir_popup("Velocidad", list(velocidad.UNIDADES.keys()), velocidad.convertir)

    def abrir_datos(self):
        self.abrir_popup("Datos", list(datos.UNIDADES.keys()), datos.convertir)

    def abrir_divisas(self):
        self.abrir_popup("Divisas", list(divisas.TASAS.keys()), divisas.convertir)

    def abrir_descuento(self):
        layout = BoxLayout(orientation="vertical", padding=15, spacing=10)

        precio = TextInput(hint_text="Precio", multiline=False, input_filter="float", font_size=22)
        porc = TextInput(hint_text="Porcentaje de descuento", multiline=False, input_filter="float", font_size=22)
        resultado = Label(text="Resultado", font_size=22)
        boton = Button(text="Calcular", font_size=20, background_color=(1, 0.45, 0.05, 1))

        def calcular(_):
            try:
                d, total = descuento.calcular(precio.text, porc.text)
                resultado.text = f"Descuento: {d}\nTotal: {total}"
            except Exception:
                resultado.text = "Valor inválido"

        boton.bind(on_press=calcular)

        layout.add_widget(Label(text="Descuento", font_size=24, bold=True))
        layout.add_widget(precio)
        layout.add_widget(porc)
        layout.add_widget(boton)
        layout.add_widget(resultado)

        Popup(title="Descuento", content=layout, size_hint=(0.9, 0.75)).open()

    def abrir_finanzas(self):
        layout = BoxLayout(orientation="vertical", padding=15, spacing=10)

        capital = TextInput(hint_text="Capital", multiline=False, input_filter="float", font_size=22)
        tasa = TextInput(hint_text="Tasa %", multiline=False, input_filter="float", font_size=22)
        tiempo_txt = TextInput(hint_text="Tiempo", multiline=False, input_filter="float", font_size=22)
        resultado = Label(text="Resultado", font_size=22)
        boton = Button(text="Calcular", font_size=20, background_color=(1, 0.45, 0.05, 1))

        def calcular(_):
            try:
                interes, total = finanzas.interes_simple(capital.text, tasa.text, tiempo_txt.text)
                resultado.text = f"Interés: {interes}\nTotal: {total}"
            except Exception:
                resultado.text = "Valor inválido"

        boton.bind(on_press=calcular)

        layout.add_widget(Label(text="Finanzas", font_size=24, bold=True))
        layout.add_widget(capital)
        layout.add_widget(tasa)
        layout.add_widget(tiempo_txt)
        layout.add_widget(boton)
        layout.add_widget(resultado)

        Popup(title="Finanzas", content=layout, size_hint=(0.9, 0.8)).open()

    def abrir_imc(self):
        layout = BoxLayout(orientation="vertical", padding=15, spacing=10)

        peso = TextInput(hint_text="Peso en kg", multiline=False, input_filter="float", font_size=22)
        altura = TextInput(hint_text="Altura en metros", multiline=False, input_filter="float", font_size=22)
        resultado = Label(text="Resultado", font_size=22)
        boton = Button(text="Calcular", font_size=20, background_color=(1, 0.45, 0.05, 1))

        def calcular(_):
            try:
                valor, estado = imc.calcular(peso.text, altura.text)
                resultado.text = f"IMC: {valor}\n{estado}"
            except Exception:
                resultado.text = "Valor inválido"

        boton.bind(on_press=calcular)

        layout.add_widget(Label(text="IMC", font_size=24, bold=True))
        layout.add_widget(peso)
        layout.add_widget(altura)
        layout.add_widget(boton)
        layout.add_widget(resultado)

        Popup(title="IMC", content=layout, size_hint=(0.9, 0.75)).open()

    def abrir_sistema(self):
        layout = BoxLayout(orientation="vertical", padding=15, spacing=10)

        entrada = TextInput(hint_text="Número decimal", multiline=False, input_filter="int", font_size=22)
        resultado = Label(text="Resultado", font_size=20)
        boton = Button(text="Convertir", font_size=20, background_color=(1, 0.45, 0.05, 1))

        def calcular(_):
            try:
                n = entrada.text
                resultado.text = (
                    f"Binario: {sistema.decimal_binario(n)}\n"
                    f"Hexadecimal: {sistema.decimal_hexadecimal(n)}\n"
                    f"Octal: {sistema.decimal_octal(n)}"
                )
            except Exception:
                resultado.text = "Valor inválido"

        boton.bind(on_press=calcular)

        layout.add_widget(Label(text="Sistema numérico", font_size=24, bold=True))
        layout.add_widget(entrada)
        layout.add_widget(boton)
        layout.add_widget(resultado)

        Popup(title="Sistema numérico", content=layout, size_hint=(0.9, 0.75)).open()

    def abrir_fecha(self):
        Popup(
            title="Fecha",
            content=Label(text="Convertidor de fecha pendiente"),
            size_hint=(0.8, 0.4)
        ).open()