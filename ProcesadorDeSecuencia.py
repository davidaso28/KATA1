
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
        elif "," in cadena:
            if(int(cadena[0])<int(cadena[2])):
                return [2,int(cadena[0]),int(cadena[2])]
            else:
                return [2, int(cadena[2]), int(cadena[0])]

        else:
            return [1,int(cadena),int(cadena)]


