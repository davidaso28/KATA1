from unittest import TestCase

from ProcesadorDeSecuencia import ProcesadorDeSecuencia
class ProcesadorDeSecuenciaTest(TestCase):
    def test_cantidadDeElementos(self):
        self.assertEqual(ProcesadorDeSecuencia().cantidadDeElementos(""),0,"Cadena vacia")
