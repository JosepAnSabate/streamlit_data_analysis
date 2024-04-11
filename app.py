import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def stats(dataframe):
    st.header('Data Statistics')
    st.write(df.describe())

def header(dataframe):
    st.header('Data Header')
    st.write(df.head())

def plot(dataframe):
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Depth'], 
               y=df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')

    st.pyplot(fig)

def interactive_plot(dataframe):
    x_axis_values = st.selectbox(
        'Select X-axis', options=dataframe.columns)

    y_axis_values = st.selectbox(
        'Select Y-axis', options=dataframe.columns)

    color = st.color_picker(
        'Pick a color', '#00f900')

    fig = px.scatter(
        dataframe, 
        x=x_axis_values, 
        y=y_axis_values)
    
    fig.update_traces(
        marker=dict(color=color)
    )
    st.plotly_chart(fig)
    
def interactive_map(dataframe):
    fig = px.scatter_mapbox(
        dataframe, 
        lat='Latitude', 
        lon='Longitude', 
        hover_name='Date', 
        zoom=1)
    fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "United States Geological Survey",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
      ])
    st.plotly_chart(fig)


    


st.title('Earthquake Data Explorer')
st.text('This is a web app to explore Earthquake datasets')

# multi page
st.sidebar.title('Navigation')

uploaded_file = st.sidebar.file_uploader("Upload your file here")

options = st.sidebar.radio('Pages',
        options=['Home', 'Data Statistics', 
                 'Data Header', 'Plot',
                 'Interactive Plot',
                 'mapa'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)


    if options == 'Data Statistics':
        stats(df)
    elif options == 'Data Header':
        header(df)
    elif options == 'Plot':
        plot(df)
    elif options == 'Interactive Plot':
        interactive_plot(df)
    elif options == 'mapa':
        interactive_map(df)