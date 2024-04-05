from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class TicTacToe(App):
    
    def build(self):
        self.Tablero = BoxLayout(orientation="vertical")
        self.current_player = 'X'  # Iniciar con el jugador X
        
        self.board_state = [['' for _ in range(3)] for _ in range(3)]  # Estado del tablero
        
        for numero_fila in range(3):
            fila = BoxLayout(orientation="horizontal")
            self.Tablero.add_widget(fila)
            for numero_columna in range(3):
                casilla = Button(font_size=80)
                casilla.bind(on_press=self.seleccionar_casilla)
                fila.add_widget(casilla)

        return self.Tablero
    
    def seleccionar_casilla(self, sender):
        fila, columna = self.obtener_posicion(sender)
        if self.board_state[fila][columna] == '':  # Verificar si la casilla está vacía
            self.board_state[fila][columna] = self.current_player  # Actualizar el estado del tablero
            if self.current_player == 'X':
                sender.text = 'X'  # Cambiar el texto del botón a X
            else:
                sender.text = 'O'  # Cambiar el texto del botón a O
            sender.disabled = True  # Deshabilitar el botón para evitar más clics
            self.toggle_player()  # Cambiar al siguiente jugador
        else:
            print("Casilla ocupada. Elija otra casilla.")

    def toggle_player(self):
        # Función para cambiar al siguiente jugador
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def obtener_posicion(self, button):
        # Función para obtener la posición de un botón en el diseño
        for i, fila in enumerate(self.Tablero.children):
            for j, widget in enumerate(fila.children):
                if widget == button:
                    return i, j
        return None, None

if __name__ == "__main__":
    TicTacToe().run()