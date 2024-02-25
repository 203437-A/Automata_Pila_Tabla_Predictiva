from tablaPredictiva import generarTabla
import re

terminales, no_terminales, tabla_predictiva = generarTabla()

class Parser:
    def __init__(self, input):
        # self.input_string = input.split()
        self.input_string = re.findall(r'\{|\}|automata|aceptacion|alfabeto|:|;|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|0|1|2|3|4|5|6|7|8|9|q|,', input)
        self.pila = ["$", "S"]
        self.recorrido = [] 

    def parse(self):
        i = 0
        try:
            while len(self.pila) > 0 and i < len(self.input_string):
                top = self.pila[-1]
                self.recorrido.append(self.pila[:])
                print(f"Pila después de procesar '{self.input_string[i]}': {' '.join(self.pila)}")
                if top in terminales:
                    if top == self.input_string[i]:
                        self.pila.pop()
                        i += 1
                    else:
                        return False
                elif top in no_terminales:
                    if self.input_string[i] in tabla_predictiva[top]:
                        produccion = tabla_predictiva[top][self.input_string[i]]
                        self.pila.pop()
                        self.pila.extend(produccion[::-1])
                    else:
                        return False
                else:
                    return False

            if len(self.pila) == 1 and self.pila[0] == "$":
                return True
            else:
                return False
        except Exception as e:
            print(f"Error: {e}")
            return False
        