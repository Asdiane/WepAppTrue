import streamlit as st
import pandas as pd


def has_headers(data):
    add_headers(data)
    return data.columns.nlevels > 1


def add_headers(data):
    if not has_headers(data):
        new_columns = [f"colonne_{i}" for i in range(1, len(data.columns) + 1)]
        data.columns = new_columns
        return data

def upload_dataset(data):
    uploaded_file = st.file_uploader("Upload your dataset (csv or excel)", type=[".csv"])
    try:
        data = pd.read_csv(uploaded_file)
        return data
    except Exception as e:
        print(e)
        st.error("Error in loading file")
            