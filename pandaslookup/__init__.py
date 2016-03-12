#!/usr/bin/env python

from pandaslookup.source import Source

def patch():
    import pandas
    from pandaslookup.table_lookup import PandasLookup

    if PandasLookup in pandas.DataFrame.__bases__:
        return

    pandas.DataFrame.__bases__ += (PandasLookup,)
