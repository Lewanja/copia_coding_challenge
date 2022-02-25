import pandas as pd


# read the table from .dat file
table = pd.read_table("weather.dat", delim_whitespace=True)

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

# find the difference between the two rows
table['spread'] = table['MxT'] - table['MnT']
max_spread_index = table['spread'].idxmax()
max_spread_value = table.iloc[max_spread_index]
print(max_spread_value['Dy'], end=' ')
print(max_spread_value['spread'])
# print(table)
