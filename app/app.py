#!/usr/bin/env python3

#importamos las librerias

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.menu import MDDropdownMenu
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
    def build(self):
        # Cargamos cada uno de los archivos .kv
        Builder.load_file('paginas/Inicio.kv')
        Builder.load_file('paginas/Configuracion.kv')
        Builder.load_file('paginas/Inventario.kv')

        return Builder.load_file('main.kv')
#aqui creo una funcion para el cambio de pantalla

    def cambiar_pantalla(self, nombre_pantalla):
        self.root.current = nombre_pantalla

#se agrega una funcionalidad para el menu desplegable

    def on_start(self):
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.menu_callback(x),
            } for i in ["Inicio", "Configuracion", "Inventario"]
        ]
        self.menu = MDDropdownMenu(
            caller=self.root.get_screen('Inicio').ids.toolbar,
            items=menu_items,
            width_mult=4,
            position="bottom"
        )

    def menu_callback(self, text_item):
        self.menu.dismiss()
        self.root.current = text_item

    def dar_clic_menu(self):
        self.menu.open()

#verificamos si se esta ejecutando como script principal

if __name__ == "__main__":
    MainApp().run()

