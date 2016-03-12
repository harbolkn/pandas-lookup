#!/usr/bin/env python

import six
import agate
import requests
import pandas as pd

from agatelookup.source import Source
from agatelookup.source import make_table_path


def make_type_tester(meta):
    """
    Uses parsed lookup table metadata create type descriptions
    for each column of the new dataframe
    """
    force = {}

    for k, v in meta["columns"].items():
        force[k] = getattr(agate, v["type"])()

    return force


class PandasSource(Source):
    """
    Pandas specific source lookup, getting a lookup table
    from @see http://wireservice.github.io/lookup
    """

    def get_table(self, keys, value, version=None):
        """
        Fetches and creates a pandas dataframe from a lookup table.
        Dataframe has row names based on the keys provided

        @param keys: list|str, columns on left side of dataframe
        @param value: str, value being looked up from the given keys
        @param version: str|None, optional version for the given lookup table
        """
        meta = self.get_metadata(keys, value, version)
        types = make_type_tester(meta)

        path = make_table_path(keys, value, version)
        url = '{}/{}'.format(self._root, path)

        if isinstance(keys, list):
            row_names = lambda r: tuple(r[k] for k in keys)
        else:
            row_names = keys

        try:
            r = requests.get(url)
            text = r.text
            self._write_cache(path, text)
        except (requests.ConnectionError, requests.Timeout):
            text = self._read_cache(path)

        if six.PY2:
            text = text.encode("utf-8")

        array = [r.split(",") for r in text.split("\n")]
        columns = array.pop(0)

        df = pd.DataFrame(array, columns=columns)
        for column, dtype in types.items():
            df[column] = df[column].apply(dtype.cast)

        return df
