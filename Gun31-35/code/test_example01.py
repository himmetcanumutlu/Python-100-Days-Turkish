# Translated to Turkish by himmetcanumutlu

"""
Birim testi - programdaki en küçük işlev modülünün (fonksiyon ve yöntem) testi
Test yöntemleri:
- Beyaz kutu testi: programın kendisi tarafından yazılan test
- Kara kutu testi: testçi veya QA, kodun uygulama ayrıntısını bilmez, yalnızca işleve odaklanır
Python birim testi yazmak - TestCase'ten kalıtım alan sınıf tanımla, test yöntemleri yaz (test_ ile başlar)
Birim testini çalıştırmak:
- unittest.main()
- python3 -m unittest test_example01.py
Üçüncü taraf kütüphaneler - nose2 / pytest
pip install pytest pytest-cov
pytest -v --cov
------------------------------
pip install nose2 cov-core
nose2 -v -C
"""
from unittest import TestCase

from example01 import seq_search, bin_search


class TestExample01(TestCase):
    """Arama fonksiyonlarını test eden test durumu"""

    # Her test fonksiyonundan önce çalıştırılacak yöntem
    def setUp(self):
        self.data1 = [35, 97, 12, 68, 55, 73, 81, 40]
        self.data2 = [12, 35, 40, 55, 68, 73, 81, 97]

    # Her test fonksiyonundan sonra çalıştırılacak yöntem
    def tearDown(self):
        pass

    def test_seq_search(self):
        """Sıralı aramayı test et"""
        self.assertEqual(0, seq_search(self.data1, 35))
        self.assertEqual(2, seq_search(self.data1, 12))
        self.assertEqual(6, seq_search(self.data1, 81))
        self.assertEqual(7, seq_search(self.data1, 40))
        self.assertEqual(-1, seq_search(self.data1, 99))
        self.assertEqual(-1, seq_search(self.data1, 7))

    def test_bin_search(self):
        """İkili aramayı test et"""
        self.assertEqual(1, bin_search(self.data2, 35))
        self.assertEqual(0, bin_search(self.data2, 12))
        self.assertEqual(6, bin_search(self.data2, 81))
        self.assertEqual(2, bin_search(self.data2, 40))
        self.assertEqual(7, bin_search(self.data2, 97))
        self.assertEqual(-1, bin_search(self.data2, 7))
        self.assertEqual(-1, bin_search(self.data2, 99))
