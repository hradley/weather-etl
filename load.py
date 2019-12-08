import glob
import logging
import os

import pandas as pd


class Loader:

    def __init__(self):
        self.__project_dir = os.path.abspath(__file__ + '/../resources')

    def save_to_parquet(self, name, file):
        file.to_parquet(self.__project_dir + '/' + name + ".parquet.gzip", engine='fastparquet', compression='GZIP')
        logging.info('Saving ' + name + ' as parquet.')

    def read_parquets(self, name):
        return [pd.read_parquet(f) for f in glob.glob(self.__project_dir + '/' + name + '*.gzip')]
