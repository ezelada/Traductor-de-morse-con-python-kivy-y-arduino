from kivy.config import Config
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '400')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import serial

class Morse(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.codigo_morse = {
            "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
            "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
            "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".--.", "q": "--.-",
            "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
            "x": "-..-", "y": "-.--", "z": "--..",
            "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
            "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
            ".": ".-.-.-", ",": "-.-.--", "?": "..--..", "\"": ".-..-."}
        self.cadena = ''
    
    def actualizar(self):
        
        try:
            self.Arduino = serial.Serial('COM5',9600)
            print("Conexión Exitosa")
            a = 0
            i = 0
            
            while a == 0:

                data = self.Arduino.readline().decode('ascii').strip()
                print(data)
                if data == "":
                    self.cadena += " "
                    i = i+1
                    if i == 2:
                        a = 1
                        i=0
                else:
                    caracter = list(self.codigo_morse.keys())[list(self.codigo_morse.values()).index(data)]
                    print(caracter)
                    self.cadena += caracter
            
        except Exception as e:
            print(e)
            print("Error al conectar")
            
        finally:
            self.cadena = self.cadena.upper()
            self.ids.respuesta.text = self.cadena
            self.Arduino.close()
            self.cadena = ''
            
    def borrar(self):
        self.ids.respuesta.text = ""


class MainApp(App):
    title="DECODIFICADOR MORSE"
    def build(self):
        return Morse()

if __name__== "__main__":
    MainApp().run()

