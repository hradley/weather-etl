import pandas as pd

from transform import Transformer


def get_hottest_day_formatted():
    transformer = Transformer()
    hottest_day = transformer.find_hottest_day()
    # rename the columns to more understandable names
    hottest_day.columns = ['Date', 'Temperature', 'Region']
    print(hottest_day.to_string(
        formatters={"Date": lambda x: "{:%d-%m-%Y}".format(pd.to_datetime(x))}, index=False))


if __name__ == '__main__':
    get_hottest_day_formatted()
