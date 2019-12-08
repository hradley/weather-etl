import glob
import os

import pandas as pd


class Extractor:

    def __init__(self):
        """
        Opens all .csv files and stores the contents in a dictionary.
        """

        self.__project_dir = os.path.abspath(__file__ + '/../')
        self.__data_sources = {os.path.basename(f): open(f) for f in
                               glob.glob(self.__project_dir + '/resources/weather*.csv')}

    def extract_csv_data(self):
        """
        Extracts the .csv files and stores them into a dict with the name of the file as a key
        and the DataFrame converted object of the file as a value.
        :return: dict containing the DataFrame data.
        """

        data = {}
        for k, v in self.__data_sources.items():
            data[k] = pd.read_csv(v)
            v.close()
        return data
