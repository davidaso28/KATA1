from unittest import TestCase

from ProcesadorDeSecuencia import ProcesadorDeSecuencia
class ProcesadorDeSecuenciaTest(TestCase):
    def test_cantidadDeElementos(self):
        self.assertEqual(ProcesadorDeSecuencia().cantidadDeElementos(""),0,"Cadena vacia")

    def test_cantidadDeElementosUnNumero(self):
        self.assertEqual(ProcesadorDeSecuencia().cantidadDeElementos("1"),1,"Cadena Un numero")

    def test_cantidadDeElementosMasDeUnNumero(self):
            self.assertEqual(ProcesadorDeSecuencia().cantidadDeElementos("1,2"), 2, "Cadena mas de un numero")

