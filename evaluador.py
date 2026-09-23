class Evaluador:
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones

    def evaluar(self) -> int | float | None:
        resultado = None
        if self.instrucciones is not None:
            for instruccion in self.instrucciones:
                resultado = instruccion.evaluar()
        return resultado
        
    