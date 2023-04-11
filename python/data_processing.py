import os
import re
import pandas as pd
import numpy as np


def read_data(path, files):
    # crime_files = subset_files(path, pattern="_\d+")
    crime_files = [os.path.join(path, file) for file in files]
    data_ls = [pd.read_csv(file, low_memory=False) for file in crime_files]
    return data_ls


def subset_files(path, pattern="_\d+"):
    files = os.listdir(path)
    return [file for file in files if re.findall(pattern, file)]


def extract_digits(files):
    return [re.findall("\d+", file).pop() for file in files]


def convert_to_datetime(data, cols):
    for col in cols:
        data[col] = pd.to_datetime(data[col])
    return data


def extract_time_of_day(disp_hour):
    dispatch_tday = np.where(
        (disp_hour >= 0) & (disp_hour < 6), 
        'night', 
        np.where(
            (disp_hour >= 6) & (disp_hour < 12), 
            'morning',
            np.where(
                (disp_hour >= 12) & (disp_hour < 18),
                'afternoon',
                'evening')))
    return dispatch_tday

def group_year(data, year):
    cut_labels = ['2006-2009', '2010-2013', '2014-2017', '2018-2022']
    cut_bins = [0, 2009, 2013, 2017, 2022]
    year_group = pd.cut(data[year], bins=cut_bins, labels=cut_labels)
    return year_group


def get_freqpct(data, by=['year_group', 'dispatch_tday']):
    data_grp = data.groupby(by).agg(
        Frequency=('year_group', 'count'),
        Percentage=('year_group', 'count')
    )
    data_grp['Percentage'] = round((data_grp['Frequency'] / data.shape[0])*100, 2)
    return data_grp