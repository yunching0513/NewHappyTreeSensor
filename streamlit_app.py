import altair as alt
import numpy as np
import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go
import time as sleep_time
from datetime import time, datetime

st.title('The Happy Tree Sensor')

import streamlit as st

st.header('2023 MADE Living Lab')

if st.button('Say hello to the Happy Trees!'):
     st.write('Hi! We are the Happy Tree team from AMS Insitute! :sunglasses::sunglasses:')
else:
     st.write('Goodbye!')

###Step 1 Building a Table 
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

###Step 2 Building a Graph

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

###Step 3 Building a Slider

     ## Sample 1
st.header('Slider')

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

     ## Sample 2

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2023, 11, 22, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

### Step 4 Building a Line Chart

st.header("Line chart")
chart_data = pd.DataFrame(
     np.random.randn(20,3),
     columns=['a','b','c']
)
st.line_chart(chart_data)


## Step 5 Building a Select Box

st.header("st.selectbox")
option = st.selectbox(
     'What kinds of data do you want to check?', ('Moisture','Temperature','Humidity','Pressure', 'Swap')
)
st.write('The Data you want to check is', option)