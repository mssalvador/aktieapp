from unittest import TestCase
from aktier.aktie.aktie import Aktie


class TestAktie(TestCase):
    def setUp(self):
        self.a = Aktie(name="test_stock", start_kurs=100., amount=100)

    def test_compute_total_volume(self):
        self.a.current_kurs = 52.3
        expected_output = 100*52.3
        output  = self.a.compute_total_volume()
        self.assertTrue(expected_output == output)