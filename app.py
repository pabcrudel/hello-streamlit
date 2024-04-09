import streamlit as st
import pandas as pd
import numpy as np

# Creates an `h1`
st.title("Hello world")

# Defines a table
df = pd.DataFrame({
    'City': ["Valencia", "Malaga"],
    'Population': [791.413, 571.026]
})

# Renders content without using Streamlit's functions
"""
This paragraph and the following table, that are a literal and a variable
respectively, are automatically printed without using `st.write()`.
"""

st.write("## Interactive Table")
df
st.write("You can accomplish that using `st.write()` too.")

st.write("## Static Table")
st.write("With the method `st.table(dl)` Streamlit generates a static table.")
st.table(df)

dataframe = pd.DataFrame(
    np.random.randn(5, 8),
    columns=('col %d' % i for i in range(8)))

st.dataframe(dataframe.style.highlight_max(axis=0))

"""
## Charts

### Line chart
"""

# Render another random chart.
# `randn()` generates an array of one or more dimensions. In this case, this
# will be a chart with 20 rows and 3 columns. Each column, or each line, will
# have a name that identifies it.
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

"""
### Maps
"""

# This chart renders a matrix of random numbers in a two-dimensional map.
# Reduces the dispersion of this points by dividing them by [50, 50].
# Then moves the generated points to the coordinates of San Francisco.
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
