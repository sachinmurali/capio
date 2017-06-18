import unittest
from src.word_extractor import WordExtractor

class TestWordExtractor(unittest.TestCase):
	def test_status_code(self):
		wex = WordExtractor()
		self.assertEquals(wex.get_transcript().status_code, 200)

	def test_time_converter(self):
		wex = WordExtractor()
		self.assertEquals(wex.get_start_time(283.6692810058594), '00:04:43.67')

if __name__ == '__main__':
	unittest.main()	