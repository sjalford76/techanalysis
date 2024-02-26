import pandas
import os
import dataaccess.environment

def get_data( data_file ):
    base_path = dataaccess.environment.Environment().get_data_path()
    df = pandas.read_csv(os.path.join(base_path, data_file), parse_dates=['Date'], dayfirst=True)
    df.sort_values(by='Date', inplace=True)

    return df
