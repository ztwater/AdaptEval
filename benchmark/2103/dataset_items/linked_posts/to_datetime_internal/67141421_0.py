import numpy as np
import pandas as pd

def dt64_to_float(dt64):
    """Converts numpy.datetime64 to year as float.

    Rounded to days

    Parameters
    ----------
    dt64 : np.datetime64 or np.ndarray(dtype='datetime64[X]')
        date data

    Returns
    -------
    float or np.ndarray(dtype=float)
        Year in floating point representation
    """

    year = dt64.astype('M8[Y]')
    # print('year:', year)
    days = (dt64 - year).astype('timedelta64[D]')
    # print('days:', days)
    year_next = year + np.timedelta64(1, 'Y')
    # print('year_next:', year_next)
    days_of_year = (year_next.astype('M8[D]') - year.astype('M8[D]')
                    ).astype('timedelta64[D]')
    # print('days_of_year:', days_of_year)
    dt_float = 1970 + year.astype(float) + days / (days_of_year)
    # print('dt_float:', dt_float)
    return dt_float

if __name__ == "__main__":

    dt_str = '2011-11-11'
    dt64 = np.datetime64(dt_str)
    print(dt_str, 'as float:', dt64_to_float(dt64))
    print()

    dates = np.array([
        '1970-01-01', '2014-01-01', '2020-12-31', '2019-12-31', '2010-04-28'],
        dtype='datetime64[D]')
    float_dates = dt64_to_float(dates)


    print('dates:      ', dates)
    print('float_dates:', float_dates)
