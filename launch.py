import pandas as pd

from transform import Transformer


def get_hottest_day_formatted():
    """
    Finds the hottest day from the two .csv data files, using the output from the Transformer.
    Prints a formatted result which is more convenient for the user.
    """

    transformer = Transformer()
    hottest_day = transformer.find_hottest_day()
    # rename the columns to more understandable names
    hottest_day.columns = ['Date', 'Temperature', 'Region']
    print(hottest_day.to_string(
        formatters={"Date": lambda x: "{:%d-%m-%Y}".format(pd.to_datetime(x))}, index=False))


if __name__ == '__main__':
    get_hottest_day_formatted()
