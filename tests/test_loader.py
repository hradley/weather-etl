import glob
import os
from unittest import TestCase

from pandas import DataFrame

from load import Loader


class LoaderTest(TestCase):

    def setUp(self):
        self.loader = Loader()
        self.project_dir = os.path.abspath(__file__ + "/../../")
        for f in glob.glob(self.project_dir + "/resources/*.parquet.gzip"):
            os.remove(f)

    def tearDown(self):
        for f in glob.glob(self.project_dir + "/resources/*.parquet.gzip"):
            os.remove(f)

    def test_save_parquet(self):
        data = DataFrame([{"key1": "value1", "key2": "value2"}])
        self.loader.save_to_parquet("test", data)
        result = os.path.isfile(self.project_dir + "/resources/test.parquet.gzip")
        self.assertTrue(result)

    def test_read_parquets(self):
        data = DataFrame([{"key1": "value1", "key2": "value2"}])
        self.loader.save_to_parquet("test", data)
        result = self.loader.read_parquets("test")
        self.assertCountEqual(data, result[0])
