from nwd import nwd, nwd_optimal, nww
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
        self.assertEqual(nww(3,4), 12)
        self.assertEqual(nww(6,4), 12)
        self.assertEqual(nww(30,36), 180)


if __name__ == '__main__':
    unittest.main()
