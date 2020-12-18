# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import numpy as np
st.title('My first app')
df=pd.DataFrame({ 'first_column':[1,2,3,4],'secound_column':[10,20,30,40]})
resmi='My wife '
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c'])
st.line_chart(chart_data)
map_data = pd.DataFrame(
    np.random.randn(1000,2)/[50,50]+[37.76,-122.4],
    columns=['lat','lon'])
st.map(map_data)
option= st.sidebar.selectbox(
    'which number do you like best?',df['first_column'])
'you selected',option
left_column,right_column=st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed :
    right_column.write("wohoo!")
expander= st.beta_expander("FAQ")
expander.write("Here you could put in some really,reallu]y long explanations")
import time
latest_iteration = st.empty()
bar =st.progress(0)
for i in range (100):
    latest_iteration.text(f'Iteration(i+1')
    bar.progress(i+1)
    time.sleep(.1)