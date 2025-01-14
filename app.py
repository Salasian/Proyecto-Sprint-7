import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # Read the data

st.header('Access to our graphics')
st.subheader('Press any button or checkbox')

build_histogram = st.checkbox('Builds a Histogram')

if build_histogram: # If the checkbox is checked
    # Write a message
    st.write('Creation of a Histogram using the data from the car sales announcements data')

    # Create a Histogram
    fig = px.histogram(car_data, x="odometer")

    # Show Plotly interactive graphic
    st.plotly_chart(fig, use_container_width=True)

build_dispersion = st.button('Build a dispersion diagram')

if build_dispersion: # If the button is clicked
    # Write a message
    st.write('Creation of a Dispersion Diagram using the data from the car sales announcements data')

    # Create a dispersion diagram
    fig = px.scatter(car_data, x="odometer", y="price")

    # Show a plotly interactive graphic
    st.plotly_chart(fig, use_container_width=True)