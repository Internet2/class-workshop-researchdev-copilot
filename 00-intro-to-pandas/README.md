# Introduction to Pandas

Below is a quick primer on pandas. The purpose of this markdown is to cover the basic concepts of pandas to set the context for the exercises that we will be undertaking in this workshop.

## What is Pandas?

Pandas is a powerful Python library used for data manipulation and analysis. It provides data structures and functions designed to work efficiently with structured data, particularly large and complex datasets.

## Key Features of Pandas

- **Data manipulation**: Perform basic and advanced data operations like merging, reshaping, selecting, as well as cleaning.
- **Time Series**: Extensive support for date-time data for financial and time-series analysis.
- **Handling Missing Data**: Convenient methods for detecting, removing, and replacing missing data.
- **Efficient I/O Tools**: Tools for reading data from a variety of formats (CSV, Excel, JSON, etc.) and writing data.

## What is a DataFrame?

A DataFrame is a two-dimensional, size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). It is arguably the most central and widely used pandas object, akin to a spreadsheet.

### Creating a DataFrame

You can create a DataFrame from various sources such as a list, dictionary, or reading from a CSV file.

```python
import pandas as pd

# Creating from a dictionary
data = {'Name': ['John', 'Anna'], 'Age': [28, 22]}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
```

### Basic DataFrame Operations
- **Viewing Data**: df.head() to see the first few rows.
- **Describing Data**: df.describe() to view summary statistics.
- **Data Selection**: df['Column'] to select a column.

### Why Use Pandas?

Pandas simplifies tasks that are complex in other languages, enabling more readable, concise, and user-friendly data manipulation code. It is an indispensable tool for data scientists due to its powerful data processing capabilities and seamless integration with other libraries.


### Further Learning

For more detailed exploration, consider checking out the [Pandas Documentation](https://pandas.pydata.org/docs/).

Also checkout an introductory guide on [Python for Data Analysis](https://wesmckinney.com/book/).
