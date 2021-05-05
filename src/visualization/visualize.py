#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os
import pandas as pd
import matplotlib.pyplot as plt


def main():
    """ Visualize resampling climate data every 1 hour. """
    logger = logging.getLogger(__name__)
    logger.info('Resampling climate data')

    ifn = f'../../data/processed/climate_1hour.parquet'
    if not os.path.isfile(ifn):
        raise Exception("There is no file {ifn}!")
    df = pd.read_parquet(ifn)

    plot_coln_l = ['T (degC)', 'p (mbar)', 'rho (g/m**3)']
    for coln_i in plot_coln_l:
        if coln_i not in df.columns:
            raise Exception(f'There is no column: {coln_i}!')

    # plot data
    df.fillna(0, inplace=True)
    ofn = '../../data/visualized/climate_1hour.png'
    df[plot_coln_l].plot(subplots=True)
    plt.savefig(ofn)
    plt.close()

    ofn = '../../data/visualized/climate_1hour_first_480_hour.png'
    df[plot_coln_l].iloc[:480].plot(subplots=True)
    plt.savefig(ofn)
    plt.close()


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
