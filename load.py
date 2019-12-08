import glob
import logging
import os

import pandas as pd


class Loader:

    def __init__(self):
        self.__project_dir = os.path.abspath(__file__ + '/../resources')

    def save_to_parquet(self, name, file):
        """
        Saves the content of each extracted file to disc in a .parquet format.
        :param name: the name of the file.
        :param file: the DataFrame content of the file.
        :return: saves the content of each file to disc in a .parquet format.
        """

        file.to_parquet(self.__project_dir + '/' + name + ".parquet.gzip", engine='fastparquet', compression='GZIP')
        logging.info('Saving ' + name + ' as parquet.')

    def read_parquets(self, name):
        """
        Reads the parquet files that match a name pattern and returns them in a list of DataFrames.
        :param name: the name of the files to match on.
        :return: a list of DataFrames containing the read parquet files.
        """

        return [pd.read_parquet(f) for f in glob.glob(self.__project_dir + '/' + name + '*.gzip')]
