import streamlit as st
import pandas as pd
import numpy as np

# Add a title
st.title("JosephOregon's First Streamlit App")


# Add some text
st.text('Data Dashing')


# Add some text
st.text('Stay Tuned, adjustments will be made -- initial test.')


calls_df = pd.read_html("http://apps.sandiego.gov/sdfiredispatch/", header=0, parse_dates=["Call Date"])

st.dataframe(calls_df)

if st.checkbox('Expand Test DataFrame'):
    st.dataframe(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40],
        'third column': [100, 200, 300, 400]
    }))

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(map_data)

df = pd.DataFrame(
np.random.randn(20, 3),
columns=['a', 'b', 'c'])

column = st.selectbox(
'Select Column To Display',
df.columns)

st.line_chart(df[column])

df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

columns = st.multiselect(
    label='What column to you want to display', options=df.columns)

st.line_chart(df[columns])

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

x = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Range values:', x)

@st.cache
def fetch_and_clean_data():
    df = pd.read_csv('<some csv>')
    # do some cleaning
    return df
