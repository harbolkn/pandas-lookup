# pandas-lookup: lookup tables for pandas

`pandaslookup` is a Python library for using [wireservice lookup tables](https://github.com/wireservice/lookup) with pandas dataframes.
Lookup is build on top of `agate-lookup`, making similar funcationality available for pandas dataframes.

## Import

```
import pandas as pd
import pandaslookup

pandaslookup.patch()
```

## Basic Lookup

```
df = pd.DataFrame({'state_abbr': ['CT', 'NY', 'NJ']})
joined = df.ws_lookup('state_abbr', 'state', lookup_key='usps')
```

## Lookup without DataFrame
Can also be used to get dataframe of an entire lookup table

```
# Get the population of each US state and territory from 1970 to 2014
population = pd.DataFrame.from_lookup(['usps', 'year'], 'population')
```

## Roadmap
* filtering table when calling `from_lookup`
