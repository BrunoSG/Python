import unittest
import PygameKawasakiTemp

class TestSequenceFunctions(unittest.TestCase):
    def test1(self):
		self.assertEqual(PygameKawasakiTemp.wrap(40), 40)

if __name__ == '__main__':
    unittest.main()