import streamlit as st
import pandas as pd
import numpy as np
from components.menu import menu_with_redirect

menu_with_redirect()

"""
# Maps
"""

# This chart renders a matrix of random numbers in a two-dimensional map.
# Reduces the dispersion of this points by dividing them by [50, 50].
# Then moves the generated points to the coordinates of San Francisco.
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
