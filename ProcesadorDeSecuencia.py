
class ProcesadorDeSecuencia:
    def cantidadDeElementos(self,cadena):
        if cadena=="":
            return 0
        else:
            return len(cadena.split(","))
