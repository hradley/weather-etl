import glob
import os

import pandas as pd


class Extractor:

    def __init__(self):
        self.__project_dir = os.path.abspath(__file__ + '/../')
        self.__data_sources = {os.path.basename(f): open(f) for f in
                               glob.glob(self.__project_dir + '/resources/weather*.csv')}

    def extract_csv_data(self):
        data = {}
        for k, v in self.__data_sources.items():
            data[k] = pd.read_csv(v)
        return data
