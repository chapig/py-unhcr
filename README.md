# UNHCR Wrapper
This is a wrapper for the UNHCR API. It is written in Python and uses the requests library to make HTTP requests to the API.

## Installation
To install the wrapper, you can use pip:

```bash
pip install unhcr-wrapper
```

## Usage
To use the wrapper, you need to import the `UNHCR` class and create an instance of it. You can then use the methods provided by the class to interact
with the API. Here is an example:

```python
from unhcr_wrapper import UNHCR

# Create an instance of the UNHCR class
unhcr = UNHCR()

# Get asylum applicants from Afghanistan in 2020 and return the data as a DataFrame
data = unhcr.set_filter(coo="AFG", year=2020).asylum_applications(dataframe=True)
```

# How to plot data
To plot the data, you can use matplotlib. Here is an example:

```python
import matplotlib.pyplot as plt
from unhcr_wrapper import UNHCR
unhcr = unhcr_client.set_filter(coo="VEN", year_from=2000, year_to=2024, coa_all=True).asylum_applications(dataframe=True)

# Group by year and sum the 'applied' values
yearly_data = unhcr.groupby('year')['applied'].sum()

# Create the plot
plt.figure(figsize=(12, 6))  # Increase figure size for better readability
yearly_data.plot(kind='line', marker='o')

# Title and labels
plt.title('Total Applications Over the Years')
plt.xlabel('Year')
plt.ylabel('Total Applications')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Optional: Limit the number of x-axis labels to avoid crowding
plt.xticks(ticks=range(min(yearly_data.index), max(yearly_data.index) + 1, 1))

# Display year labels on each point
for x, y in zip(yearly_data.index, yearly_data):
    plt.text(x, y, str(x), fontsize=10, ha='right', va='bottom')

# Show the grid for better visibility
plt.grid(True)

# Show the plot
plt.show()
```

This would output a line plot showing the total number of applications over the years for the specified country.
![Total Applications Over the Years](https://github.com/chapig/py-unhcr/blob/main/example/output.png)

# This is a WIP
This project is a work in progress and more features will be added in the future. If you have any suggestions or feedback, feel free to open an issue or submit a pull request.
```