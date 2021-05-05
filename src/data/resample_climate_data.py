#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import pandas as pd
import os

def main():
    """ Resample climate data every 1 hour.  """
    logger = logging.getLogger(__name__)
    logger.info('resample climate data')

    ifn = '../../data/raw/climate.parquet'
    if not os.path.isfile(ifn):
        raise Exception("There is no file: {ifn}!")
    df = pd.read_parquet(ifn)

    df = df.resample('60min', closed='right', label='right').last()

    ofn = '../../data/processed/climate_1hour.parquet'
    df.to_parquet(ofn)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
