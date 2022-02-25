# WEATHER DATA

## Exercise

*The accompanying file weather.dat contains weather data for a single month as space-separatedvalues. The first column (Dy) contains the day  of the month; the second (MxT) contains the maximum temperature for that day, while the third (MnT) contains the minimum temperature.The final row contains aggregate values for the entire month. Write a program to find the row with the maximum spread in the weather.dat file, where spread is defined as the difference between MxT and MnT. For example, the spread for day 2 was (79 - 63) = 16. Your program should print the day of the month and spread to standard output. Assuming that your program is called weather.py, then a sample run will look like:

```python 
python weather.py
 $ : 2 16
 ```
where 2 is the day of the month with the maximum spread, and the actual spread is 16. (The actual
day and spread will depend on the contents of the file.)*

## Solution

#### Requirements

1. [Pandas Library](https://pypi.org/project/pandas/)

```sh
pip install pandas
```

### Project

Import pandas libraries to the IDE.

```python
import pandas as pd
```

Reading data from the file using Pandas:

`read_table()` is used since the data is from a tabulated file and contains a header row. Whitespaces are present on the header of row of the column therefore, `delim_whitespace=True` is used.

  ```python
 # read the table from .dat file
table = pd.read_table("weather.dat", delim_whitespace=True)
 ```

Determine maximum spread:

Values read from weather.data file are strings. To perfom mathematical operations, our values have to be floats. However we cannot convert some values directly as they have an asteric(*).

```sh
AttributeError: '*' is not a valid function for 'Series' object 
```

 We therefore have to do some cleaning and then use  `.astype(float)` to change it to a float.
 
 
  We then find all the spreads by finding the difference between max and min temperature and then find the max spread.



Thus, the clean integer function is defined to eliminate the '*' which is substituted with an empty space and called inside the apply function `.apply(clean_integers)`.

```python

def clean_integers(x):
    x = str(x).replace("*", "")
    if x == "":
        x = 0
    return x

# # # some values have * remove them
table['MxT'] = table['MxT'].apply(clean_integers)
table['MnT'] = table['MnT'].apply(clean_integers)

# convert strings to floats to allow mathematical operations on them
table['MxT'] = table['MxT'].astype(float)
table['MnT'] = table['MnT'].astype(float)
```

The difference between the maximum temperature and minimum temperature is performed and a column containing the results tabulated. `table['spread']`.

```python

# find the difference between the two rows
table['spread'] = table['MxT'] - table['MnT']
max_spread_index = table['spread'].idxmax()
```

The `idxmax()` is used to get the row with maximum value on *spread* column. The specific column containg the value of day(Dy) and difference in temperatures (spread) is captured using `max_spread_value['Dy'], end=' ')` `print(max_spread_value['spread` functions.

```python
max_spread_value = table.iloc[max_spread_index]
print(max_spread_value['Dy'], end=' ')
print(max_spread_value['spread'])
print(table)
```

Output from the code is: `11 91.0`
