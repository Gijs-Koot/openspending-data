# `openspending-data`

Python wrapper for accessing the OpenSpending API. Not complete at all, only works for the `governments` and `entries` endpoints, see https://openspending.nl/api/v1 for documentation of these. 

## Installation

```
pip install git+https://github.com/Gijs-Koot/openspending-data
```

## Usage

```
from openspending import OpenSpending

os = OpenSpending()

# retrieve all governments
govs = os.governments(params={}, max=800) # returns a list

# retrieve all entries from a specific year from a specific gov body
entries = os.entries(params=dict(year=2016, gov_code=358, max=20000) # returns a list
```

