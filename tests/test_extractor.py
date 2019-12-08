from unittest import TestCase

from extract import Extractor


class TestExtractor(TestCase):

    def setUp(self):
        self.extractor = Extractor()

    def test_extract_csv_data(self):
        result = self.extractor.extract_csv_data()
        self.assertCountEqual(['weather.20160201.csv', 'weather.20160301.csv'], result.keys())
