#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import tensorflow as tf
import datetime
import pandas as pd
import os

CLIMATE_DATA_URL = 'https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip'

def main():
    """ Download climate data.  """
    logger = logging.getLogger(__name__)
    logger.info('download climate data')

    zip_path = tf.keras.utils.get_file(
        origin=CLIMATE_DATA_URL,
        fname=CLIMATE_DATA_URL.split('/')[-1],
        extract=True,
    )
    f = lambda x: datetime.datetime.strptime(x, '%d.%m.%Y %H:%M:%S')
    df = pd.read_csv(os.path.splitext(zip_path)[0], parse_dates=[0], index_col=[0], date_parser=f, na_values=-9999)

    ofn = '../../data/raw/climate.parquet'
    df.to_parquet(ofn)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
