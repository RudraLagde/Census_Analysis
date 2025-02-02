import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv("india.csv")

list_of_states = list(df["State"].unique())
list_of_states.insert(0, "Overall India")
parameters = sorted(df.columns[5:])

st.sidebar.title("India")

selected_state = st.sidebar.selectbox("Select a state", list_of_states)
primary = st.sidebar.selectbox("Select Primary Parameter" ,parameters)
secondary = st.sidebar.selectbox("Select Secondary Parameter" ,parameters)

plot = st.sidebar.button('Plot Graph')

if plot:
    if selected_state == 'Overall India':
        #we will plot for overall india
        fig = px.scatter_mapbox(df , lat='Latitude', lon='Longitude', zoom=3.5,mapbox_style='carto-positron', size = primary , color=secondary , hover_name='District', color_continuous_scale="Plasma")
        fig.update_layout(height=650)  # Adjust height as needed
        st.plotly_chart(fig , use_container_width=True)
    else:
        # we will plot for state
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', zoom=6, mapbox_style='carto-positron',size=primary, color=secondary , hover_name='District', color_continuous_scale="Plasma")
        fig.update_layout(height=650)

        st.plotly_chart(fig, use_container_width=True)
