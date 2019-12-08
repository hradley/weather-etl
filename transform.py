import pandas as pd

from load import Loader
from extract import Extractor


class Transformer:

    def __init__(self):
        self.__data = Extractor().extract_csv_data()
        self.__loader = Loader()
        # save all extracted DataFrames from csv files to parquet files
        for k, v in self.__data.items():
            self.__loader.save_to_parquet(k, v)
        # reads all saved parquet files
        data_files = self.__loader.read_parquets("weather")
        # combines all DataFrames into one
        self.__df = pd.concat(data_files, ignore_index=True)

    def find_hottest_day(self):
        # creates a subset of the data with only the columns we need
        df_subset = self.__df[['ObservationDate', 'ScreenTemperature', 'Region']]
        # find the row with max temperature
        return df_subset[df_subset['ScreenTemperature'] == df_subset['ScreenTemperature'].max()]
