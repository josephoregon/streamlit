import streamlit as st
import pandas as pd
import numpy as np

# Add a title
st.title("JosephOregon's First Streamlit App")


# Add some text
st.text('Data Dashing')


# Add some text
st.text('Stay Tuned, adjustments will be made -- initial test.')

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

@st.cache
def load_data(nrows):

data_load_state.text("Done! (using st.cache)")

st.subheader('Number of pickups by hour')

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

st.subheader('Map of all pickups')

st.map(data)

st.subheader('Map of all pickups')
st.map(data)

hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

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
