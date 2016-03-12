#!/usr/bin/env python

import pandas as pd

from pandaslookup.source import PandasSource

DEFAULT_SOURCE = PandasSource()


class PandasLookup(object):
    def ws_lookup(self, key, value,
                  lookup_key=None,
                  version=None,
                  source=None,
                  require_match=False):
        if source is None:
            source = DEFAULT_SOURCE

        table = source.get_table(lookup_key or key, value, version)

        if isinstance(lookup_key, list):
            table.rename(columns={lookup_key[i]: key[i] for i in range(len(lookup_key))}, inplace=True)
        else:
            table.rename(columns={lookup_key: key}, inplace=True)

        return pd.merge(self, table, how="left")

    @classmethod
    def from_lookup(cls, lookup_key, value, version=None, source=None):
        """
        Fetch a lookup table but don't join it to anything
        """
        if source is None:
            source = DEFAULT_SOURCE

        return source.get_table(lookup_key, value, version)
