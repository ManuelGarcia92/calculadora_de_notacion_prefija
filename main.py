texto = "[*[-32]4]"
lista_tokens = []
for token in texto:
    lista_tokens.append(token)
lista_tokens.append("FIN")

class calculadora_simple:
    def __init__(self, operador, numeros):
        self.numeros = numeros
        self.operador = operador
        self.operacion = {
            "+" : self.sumar,
            "-" : self.restar,
            "*" : self.multiplicar,
            "/" : self.dividir
        }

    def evaluar(self):
        return self.operacion[self.operador]()
    
    def sumar(self):
        resultado = 0
        for numero in self.numeros:
            resultado += numero.evaluar()
        return resultado
    
    def restar(self):
        resultado = self.numeros[0].evaluar()
        i = 0
        while i < len(self.numeros):
            if i < len(self.numeros) - 1:
                resultado -= self.numeros[i+1].evaluar()
            i += 1
        return resultado
    
    def multiplicar(self):
        resultado = 1
        for numero in self.numeros:
            resultado *= numero.evaluar()
        return resultado
    
    def dividir(self):
        resultado = self.numeros[0].evaluar()
        i = 0
        while i < len(self.numeros):
            if i < len(self.numeros) - 1:
                resultado /= self.numeros[i+1].evaluar()
            i += 1
        return resultado
    
class NodoOperacion:
    def __init__(self, operador):
        self.operador = operador
        self.hijos = []

    def evaluar(self):
        calculadora = calculadora_simple(self.operador, self.hijos)
        return calculadora.evaluar()

class NodoNumero:
    def __init__(self, valor):
        self.valor = valor

    def evaluar(self):
        return float(self.valor)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.limite = len(tokens)
        self.pos = 0

    def advance(self):
        if self.pos < self.limite:
            token = self.tokens[self.pos]
            self.pos += 1
            return token
        return None

    def peek(self, pasos=0):
        if self.pos < self.limite:
            return self.tokens[self.pos + pasos]
        return None

    def match(self, tipo, pasos=0):
        token = self.peek(pasos)
        if token == tipo:
            return token
        return None 

    def consumir(self, tipo, mensaje_error):
        if self.match(tipo):
            return self.advance()
        raise Exception(mensaje_error) 

    def parsear(self):
        if self.match("FIN"):
            raise Exception("Expresión vacia")
        
        arbol = self.expre()

        if self.peek() and not self.match("FIN"):
            raise Exception("Quedan tokens sin procesar")
    
        return arbol
    
    def expre(self):
        self.consumir("[", "La operación debe empezar con un [")
        operador = self.advance()
        nodo = NodoOperacion(operador)

        while not self.match("]"):
            nodo.hijos.append(self.factor())

        self.consumir("]", "La operación debe terminar con un ]")
        return nodo
    
    def factor(self):
        if self.match("["):
            return self.expre()
        else:
            token = self.advance()
            return NodoNumero(token)

try:
    parser = Parser(texto)
    arbol = parser.parsear()
    resultado = arbol.evaluar()
    print(resultado)
except Exception as error:
    print(error)
