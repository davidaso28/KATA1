
class ProcesadorDeSecuencia:
    def cantidadDeElementos(self,cadena):
        if cadena=="":
            return [0]
        else:
            return len(cadena.split(","))

    def cantidadDeElementosYminimo(self,cadena):
        if cadena == "":
            return [0,None]
        else:

            return [len(cadena.split(",")),min(map(int,cadena.split(",")))]

    def cantidadDeElementosYMaximo(self,cadena):
        if cadena == "":
            return [0,None,None]
        else:
            return [len(cadena.split(",")),min(map(int,cadena.split(","))),max(map(int,cadena.split(",")))]

    def cantidadMinimoMaximoPromedio(self,cadena):
        if cadena=="":
            return[0,None,None,None]
        else:
            return [1,int(cadena),int(cadena),int(cadena)]


