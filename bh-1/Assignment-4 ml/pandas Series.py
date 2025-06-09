# (a) Create a Series from the list [7, 11, 13, 17].
# (b) Create a Series with five elements where each element is 100.0.
# (c) Create a Series with 20 elements that are all random numbers in the range 0 to 100. Use the
# describe method to produce the Series’ basic descriptive statistics.
# (d) Create a Series called temperatures with the following floating-point values: 98.6, 98.9,
# 100.2, and 97.9. Use the index keyword argument to specify the custom indices ’Julie’,
# ’Charlie’, ’Sam’, and ’Andrea’.
# (e) Form a dictionary from the names and values in Part (d), then use it to initialize a Series.


import pandas as pd
import numpy as np
# (a)
series_a = pd.Series([7, 11, 13, 17])
print("Series a:\n", series_a, "\n")
# (b)
series_b = pd.Series([100.0] * 5)
print("Series b:\n", series_b, "\n")
# (c)
series_c = pd.Series(np.random.randint(0, 101, size=20))
print("Series c:\n", series_c, "\n")
print("Descriptive statistics:\n", series_c.describe(), "\n")
# (d)
temperatures = pd.Series(
    [98.6, 98.9, 100.2, 97.9],
    index=['Julie', 'Charlie', 'Sam', 'Andrea']
)
print("Series d:\nTemperatures Series:\n", temperatures, "\n")
# (e)
temp_dict = temperatures.to_dict()
series_from_dict = pd.Series(temp_dict)
print("Series e:\nSeries from dictionary:\n", series_from_dict)
