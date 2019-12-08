from unittest import TestCase

from transform import Transformer


class TestTransformer(TestCase):

    def setUp(self):
        self.transformer = Transformer()

    def test___init__(self):
        result = self.transformer.find_hottest_day()
        print(result)
        self.assertEqual(1, len(result.index))
        self.assertEqual('2016-03-17T00:00:00', str(result['ObservationDate'].iloc[0]))
        self.assertEqual(15.8, float(result['ScreenTemperature'].iloc[0]))
        self.assertEqual('Highland & Eilean Siar', str(result['Region'].iloc[0]))
