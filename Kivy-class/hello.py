# hello.py
#
# Aplicación Kivy Mínima
#
# Para poder ejecutar, primero debe haber instalado Kivy en el proyecto
# usando el comando
#
#     pip install "kivy[base]"  
#

# Para poder utilizar Kivy en su aplicación, lo primero es importar
# la clasee App del módulo kivy.app
from kivy.app import App

# Cada componente que vaya a utilizar, debe ser importado 
from kivy.uix.label import Label


from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
# Cada aplicación Kivy es una clase descendiente de la clase kivy.app.App
class HelloApp(App):
    
    # El método Build es el encargado de crear los controles visuales
    # que comprenden la ventana principal de la aplicación
    def build(self):
        contenedor=BoxLayout(orientation="vertical")
        fila1=BoxLayout(orientation="horizontal")
        Window.clearcolor = ("white")
        # build() debe retornar el componente que contiene a todos los
        # demás controles de la ventana
        
        for _ in range (3):
            etiqueta=Label(text="X", font_size=80, color= "blue", bold=True)
            fila1.add_widget(etiqueta)
            contenedor.add_widget(fila1)

        return contenedor
        
        
        
    
app=HelloApp()
app.run()