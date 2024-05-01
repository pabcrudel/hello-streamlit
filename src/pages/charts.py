import streamlit as st
import pandas as pd
import numpy as np
from components.header import main_header

main_header("Charts")

"""
## Line chart
"""

# Render another random chart.
# `randn()` generates an array of one or more dimensions. In this case, this
# will be a chart with 20 rows and 3 columns. Each column, or each line, will
# have a name that identifies it.
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
