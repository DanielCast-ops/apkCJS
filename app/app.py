#!/usr/bin/env python3

#importamos las librerias

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#Definimos cada una de las pantallas

class Inicio(Screen):
    pass

class Configuracion(Screen):
    pass

class Inventario(Screen):
    pass

#en este espacio se crea la aplicacion principal

class MainApp(MDApp):
    def construir(self):
        self.load_all_kv_files()
        return Builder.load_file('main.kv')

    def cargar_documentos(self):
        Builder.load_file('paginas/Inicio.kv')
        Builder.load_file('paginas/Configuracion.kv')
        Builder.load_file('paginas/Inventario.kv')

    def dar_clic_menu(self):
        print("al menu")

#aqui creo una funcion para el cambio de pantalla

    def cambiar_pantalla(self, nombre_pantalla):
        self.root.current = nombre_pantalla


#verificamos si se esta ejecutando como script principal

if __name__ == "__main__":
    MainApp().run()

