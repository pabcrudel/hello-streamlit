import streamlit as st
import pandas as pd
import numpy as np

# Creates an `h1`
st.title("Hello Streamlit")

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
