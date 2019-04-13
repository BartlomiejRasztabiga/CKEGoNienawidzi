from nwd import nwd, nwd_optimal, nww
from fibonacci import fibo
from wydawanie_reszty_zachlanny import wydawanie
from min_max import min_max
from sortowanie import babelek_sort
from pierwiastek import pierwiastek
from horner import horner
from potegowanie_szybkie import szybkie
from miejsca_zerowe_f import zerowe
from calkowanie import prostokatow
from palindrom import palindrom

import unittest


class TestAlgorithms(unittest.TestCase):

    def test_nwd(self):
        self.assertEqual(nwd(150, 120), 30)
        self.assertEqual(nwd(198, 231), 33)
        self.assertEqual(nwd(70, 28), 14)
        self.assertEqual(nwd(550, 325), 25)

    def test_nwd_optimal(self):
        self.assertEqual(nwd_optimal(150, 120), 30)
        self.assertEqual(nwd_optimal(198, 231), 33)
        self.assertEqual(nwd_optimal(70, 28), 14)
        self.assertEqual(nwd_optimal(550, 325), 25)

    def test_nww(self):
        self.assertEqual(nww(3, 4), 12)
        self.assertEqual(nww(6, 4), 12)
        self.assertEqual(nww(30, 36), 180)

    def test_fibonacci(self):
        self.assertEqual(fibo(1), 1)
        self.assertEqual(fibo(2), 1)
        self.assertEqual(fibo(5), 5)
        self.assertEqual(fibo(18), 2584)

    def test_wydawanie(self):
        self.assertEqual(wydawanie(129), [0, 0, 1, 0, 1, 0, 1, 2, 0])
        self.assertEqual(wydawanie(69420), [138, 2, 0, 0, 1, 0, 0, 0, 0])
        self.assertEqual(wydawanie(1337), [2, 1, 1, 0, 1, 1, 1, 1, 0])

    def test_min_max(self):
        self.assertEqual(min_max([0, 0, 0, 0, -1, 1, 5, -1, 200, 5, -90]), (-90, 200))
        self.assertEqual(min_max([0]), (0, 0))
        self.assertEqual(min_max([1, 1]), (1, 1))

    def test_babelek_sort(self):
        self.assertEqual(babelek_sort([-5, 6, 932, -5632, 237, 0]), [-5632, -5, 0, 6, 237, 932])
        self.assertEqual(babelek_sort([1, 0, 0, 0, 1, 1, -1]), [-1, 0, 0, 0, 1, 1, 1])

    def test_pierwiastek(self):
        self.assertEqual(pierwiastek(3, 0.0001), 1.7320508100147274)

    def test_horner(self):
        self.assertEqual(horner([1, 0, 0, 1], 3, 1), 2)

    def test_potegowanie_szybkie(self):
        self.assertEqual(szybkie(100, 10), 100000000000000000000)
        self.assertEqual(szybkie(2, 10), 1024)

    def test_zerowe(self):
        self.assertEqual(zerowe(0, 10, 0.0000001), 2.4142135307192802)
        self.assertEqual(zerowe(-3, 0, 0.0000001), -0.4142135828733444)

    def test_calkowanie(self):
        self.assertEqual(prostokatow(1, 3, 1000), 8.666665999999699)

    def test_palindrom(self):
        self.assertTrue(palindrom("kajak"))
        self.assertFalse(palindrom("dupa"))


if __name__ == '__main__':
    unittest.main()
