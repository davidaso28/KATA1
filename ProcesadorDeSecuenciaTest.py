from unittest import TestCase

from ProcesadorDeSecuencia import ProcesadorDeSecuencia
class ProcesadorDeSecuenciaTest(TestCase):

    #Iteracion uno cantidad de elementos
    def test_cantidadDeElementos(self):
        self.assertEqual(ProcesadorDeSecuencia().cantidadDeElementos(""),[0],"Cadena vacia")

    def test_cantidadDeElementosUnNumero(self):
        self.assertEqual(ProcesadorDeSecuencia().cantidadDeElementos("1"),1,"Cadena Un numero")

    def test_cantidadDeElementosMasDeUnNumero(self):
        self.assertEqual(ProcesadorDeSecuencia().cantidadDeElementos("1,2"),2, "Cadena mas de un numero")

    def test_cantidadDeElementoNNumeros(self):
        self.assertEqual(ProcesadorDeSecuencia().cantidadDeElementos("1,2,3,4,5,6,7,8"),8, "Cadena n numeros")

    #Iteracion dos Cantidad de elementos y minimo
    def test_cantidadDeElementosMinimo(self):
            self.assertEqual(ProcesadorDeSecuencia().cantidadDeElementosYminimo(""), [0,None], "Cadena vacia")

    def test_cantidadDeElementosMinimoUnNumero(self):
        self.assertEqual(ProcesadorDeSecuencia().cantidadDeElementosYminimo("3"),[1,3],"Cadena Un numeros")

    def test_cantidadDeElementosMinimoDosNumeros(self):
        self.assertEqual(ProcesadorDeSecuencia().cantidadDeElementosYminimo("3,2"), [2,2], "Cadena dos numero")

    def test_cantidadDeElementosMinimoNNumeros(self):
            self.assertEqual(ProcesadorDeSecuencia().cantidadDeElementosYminimo("3,2,5"), [3, 2], "Cadena N numero")


    ##Iteracion tres candidad de elementos minimo y maximo
    def test_cantidadDeElementosMinimoMaximo(self):
                self.assertEqual(ProcesadorDeSecuencia().cantidadDeElementosYMaximo(""), [0, None,None], "Cadena vacia minimo maximo")


