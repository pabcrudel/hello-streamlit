from typing import List
import pandas as pd
import streamlit as st


def get_selection(df: pd.DataFrame, df_columns: List[str]):
    with st.expander("Configuration", expanded=False):
        filtered_df = df.loc[:, df_columns]

        tabs = st.tabs([df_column for df_column in df_columns])

        selections = {}

        for tab, df_column in zip(tabs, filtered_df):
            with tab:
                tab_selections = {}

                for item in filtered_df[df_column].unique().tolist():
                    if item is None:
                        item = "Unknown"

                    tab_selections[item] = st.toggle(item, True)

                selections[df_column] = tab_selections

    return selections


def filter_selection(df: pd.DataFrame, selections: dict):
    for column, values in selections.items():
        selected_values = [
            None if value == "Unknown" else value
            for value, selected in values.items() if selected
        ]
        df = df[df[column].isin(selected_values)]
    return df
