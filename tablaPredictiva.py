def generarTabla():
      terminales = ["{", "automata", "aceptacion", "alfabeto", "}", ":", ";", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "x", "y", "z","0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "q", ","]
      no_terminales = ["S", "I", "A", "B", "V", "AL", "F", "G", "SM", "RA", "C", "N", "D", "R"]

      tabla_predictiva = {
      "S": {"{": ["I", "A", "B", "V"],
            "automata": None,
            '}': None,
            ":": None,
            ";": None,
            "alfabeto": None,
            "aceptacion": None,
            "q": None,
            ",": None
            },

      "A": {"automata": ["automata"],
            "}": None,
            ":": None,
            ";": None,
            "alfabeto": None,
            "aceptacion": None,
            "q": None,
            ",": None,
            "{": None
            },

      "V": {"}": ["}"],
            "automata": None,
            ":": None,
            ";": None,
            "alfabeto": None,
            "aceptacion": None,
            "q": None,
            ",": None,
            "{": None
            },

      "B": {"alfabeto": ["AL", "F"],
            "automata": None,
            "}": None,
            ":": None,
            ";": None,
            "aceptacion": None,
            "q": None,
            ",": None,
            "{": None
            }, 

      "AL": {"alfabeto": ["G", ":", "SM", "RA", ";"],
            "automata": None,
            "}": None,
            ":": None,
            ";": None,
            "aceptacion": None,
            "q": None,
            ",": None,
            "{": None
            },

      "G": {"alfabeto": ["alfabeto"],
            "automata": None,
            "}": None,
            ":": None,
            ";": None,
            "aceptacion": None,
            "q": None,
            ",": None,
            "{": None
            },

      "SM": {"a": ["a"], "b": ["b"], "c": ["c"], "d": ["d"], "e": ["e"], "f": ["f"], "g": ["g"], "h": ["h"], "i": ["i"], "j": ["j"], "k": ["k"], "l": ["l"], "m": ["m"], "n": ["n"], "o": ["o"], "p": ["p"], "q": ["q"], "r": ["r"], "s": ["s"], "t": ["t"], "u": ["u"], "v": ["v"], "w": ["w"], "x": ["x"], "y": ["y"], "z": ["z"],
            "0": ["0"],"1": ["1"], "2": ["2"], "3": ["3"], "4": ["4"], "5": ["5"], "6": ["6"], "7": ["7"], "8": ["8"], "9": ["9"],
            "automata": None,
            "}": None,
            ":": None,
            ";": None,
            "aceptacion": None,
            "q": None,
            ",": None,
            "{": None
            },

      "RA": {",": [",", "SM", "RA"],
            "alfabeto": None, 
            "automata": None,
            "}": None,
            ":": None,
            ";": [],
            "aceptacion": None,
            "q": None,
            "{": None
            },

      "F": {"aceptacion": ["C", ":", "N", "R", ";"],
            "alfabeto": None,
            "automata": None,
            "}": None,
            ":": None,
            ";": None,
            "q": None,
            ",": None,
            "{": None
            },

      "C": {"aceptacion": ["aceptacion"],
            "alfabeto": None,
            "automata": None,
            "}": None,
            ":": None,
            ";": None,
            "q": None,
            ",": None,
            "{": None
            },

      "N": {"q": ["q", "D"],
            "alfabeto": None,
            "automata": None,
            "}": None,
            ":": None,
            ";": None,
            "aceptacion": None,
            ",": None,
            "{": None
            },

      "D": {"0": ["0"],"1": ["1"], "2": ["2"], "3": ["3"], "4": ["4"], "5": ["5"], "6": ["6"], "7": ["7"], "8": ["8"], "9": ["9"],
            "alfabeto": None,
            "automata": None,
            "}": None,
            ":": None,
            ";": None,
            "aceptacion": None,
            ",": None,
            "q": None,
            "{": None
            },

      "R": {";": [], 
            ",": [",", "N", "R"],
            "alfabeto": None,
            "automata": None,
            "}": None,
            ":": None,
            "q": None,
            "aceptacion": None,
            "{": None
            },

      "I": {"{": ["{"],
            "automata": None,
            '}': None,
            ":": None,
            ";": None,
            "alfabeto": None,
            "aceptacion": None,
            "q": None,
            ",": None
            },
      }
      return terminales, no_terminales, tabla_predictiva
