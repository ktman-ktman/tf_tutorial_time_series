#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas as pd
from cls import WindowGenerator

def main():

    # load dataset
    ifn = '../../data/processed/train.parquet'
    if not os.path.isfile(ifn):
        raise Exception(f"There is no file: {ifn}!")
    normalized_train_df = pd.read_parquet(ifn)
    ifn = '../../data/processed/valid.parquet'
    if not os.path.isfile(ifn):
        raise Exception(f"There is no file: {ifn}!")
    normalized_valid_df = pd.read_parquet(ifn)
    ifn = '../../data/processed/test.parquet'
    if not os.path.isfile(ifn):
        raise Exception(f"There is no file: {ifn}!")
    normalized_test_df = pd.read_parquet(ifn)

    w1 = WindowGenerator(24, 1, 24, normalized_train_df, normalized_valid_df, normalized_test_df, label_columns=['T (degC)'])
    print(w1)


if __name__ == '__main__':
    main()