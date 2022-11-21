
from re import U
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

def get_slice_membership(df, cities_Options ):
    """
    Implement a function that computes which rows of the given dataframe should
    be part of the slice, and returns a boolean pandas Series that indicates 0
    if the row is not part of the slice, and 1 if it is part of the slice.
    
    In the example provided, we assume genders is a list of selected strings
    (e.g. ['Male', 'Transgender']). We then filter the labels based on which
    rows have a value for gender that is contained in this list. You can extend
    this approach to the other variables based on how they are returned from
    their respective Streamlit components.
    """
    labels = pd.Series([1] * len(df), index=df.index)

    if cities_Options:
        labels &= df['city'].isin(cities_Options)
    else:
        labels = df['city'].isin(df['city'])
    return labels



st.header('Carbon Forecasting Tool')

# data source =https://www.kaggle.com/datasets/juanmah/world-cities
df = pd.read_csv("https://raw.githubusercontent.com/NikitaKhatwani/Trial/main/world-cities%20-%20world-cities.csv")
cities_Options = st.selectbox("City",df["city"].unique())
program_Options = st.selectbox("Program",df["Program"].unique())
#st.text("Area")

area = st.slider('Area (sq.m)', min_value=int(100),
                       max_value=int(100000))

# st.write(area,"sq.m")

slice_type_labels = get_slice_membership(df,[cities_Options])



df['lat'] = df['lat'].astype(int)
df['lon'] = df['lon'].astype(int)

df2 = pd.DataFrame( df[slice_type_labels][['lat','lon']])

st.map(df2)


if st.button('Calulate Carbon'):
    st.write("Your building has a carbon footprint of 80 tonnes CO2e but don't lose hope.")

