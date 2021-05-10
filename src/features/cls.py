#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class WindowGenerator:
    def __init__(self, input_width: int, label_width: int, shift: int, train_df: pd.DataFrame, val_df: pd.DataFrame, test_df: pd.DataFrame, label_columns: str = None):
        # store the raw data.
        self.train_df = train_df
        self.val_df = val_df
        self.test_df = test_df

        # work out the label column indices.
        self.label_columns = label_columns
        if label_columns is not None:
            self.label_columns_indices = {name: i for i, name in enumerate(label_columns)}

        self.column_indicies = {name: i for i in enumerate(train_df.columns)}

        # work out the window parameters.
        self.input_width = input_width
        self.label_width = label_width
        self.shift = shift

        self.total_window_size = input_width + shift

        self.input_slice = slize(0, input_width)
        self.input_indices = np.arange(self.total_window_size)[self.input_slice]

        self.label_start = self.total_window_size - self.label_width
        self.labels_slice = slice(self.label_start, None)
        self.label_indices = np.arange(self.total_window_size)[self.labels_slice]

    def __repr__(self) -> list:
        return '\n'.join([
            f'Total window size: {self.total_window_size}',
            f'Input indices: {self.input_indices}',
            f'Label indices: {self.label_indices}',
            f'Label column name(s): {self.label_columns}',
        ])