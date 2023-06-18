import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

def main():
    df = load_data()

    st.dataframe(df)

if __name__ == '__main__':
    print()