import streamlit as st
import pandas as pd 
import numpy as np

# Make a title for the webpage
st.title('Uber pickups in NYC')

# Load in data from AWS 
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# Load the data in and put it in a pandas dataframe. Convert the date column into datetime.
# Accept a single parameter in the function
# Cache the data
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')

# Load 10,000 rows of data into the dataframe
data = load_data(10000)

# Notify the reader that the data was successfully loaded.
data_load_state.text('Done! (using st.cache)')

# Look at the raw data under the subheader
### st.subheader('Raw Data')
### st.write(data)
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Draw a histogram 
st.subheader('Number of pickups by the hour')

# Use Numpy to generate a histogram that breaks down pickup times binned by hours
hist_values = np.histogram(
            data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)

#Use the st.map function to show pickup concentration
### st.subheader('Map of all pickups')
### st.map(data)
hour_to_filter = st.slider('hour', 0, 23, 17) # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)