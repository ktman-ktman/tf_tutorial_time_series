#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas as pd
import click
from sklearn.preprocessing import StandardScaler

@click.command()
@click.option("--training", type=float, default=0.7)
@click.option("--validation", type=float, default=0.2)
@click.option("--test", type=float, default=0.1)
def main(training: float, validation: float, test: float):
    if training + validation + test == 1:
        raise Exception("Dataset ratio error!")

    # read dataset
    ifn = '../../data/processed/climate_1hour.parquet'
    if not os.path.isfile(ifn):
        raise Exception(f"There is no file: {ifn}")
    df = pd.read_parquet(ifn)

    # divide dataset
    columns_indices = {name: i for i, name in enumerate(df.columns)}

    n = df.shape[0]

    train_df = df.iloc[:int(n*training)]
    valid_df = df.iloc[int(n*training):int(n*(training+validation))]
    test_df = df.iloc[int(n*(training+validation)):]

    num_features = df.shape[1]

    # normalize data
    scaler = StandardScaler()
    scaler.fit(train_df)

    normalized_train_df = train_df.copy()
    normalized_train_df.loc[:, :] = scaler.transform(train_df)
    normalized_valid_df = valid_df.copy()
    normalized_valid_df.loc[:, :] = scaler.transform(valid_df)
    normalized_test_df = test_df.copy()
    normalized_test_df.loc[:, :] = scaler.transform(test_df)
    
    ofn = '../../data/processed/train.parquet'
    normalized_train_df.to_parquet(ofn)
    ofn = '../../data/processed/valid.parquet'
    normalized_valid_df.to_parquet(ofn)
    ofn = '../../data/processed/test.parquet'
    normalized_test_df.to_parquet(ofn)


if __name__ == '__main__':
    main()