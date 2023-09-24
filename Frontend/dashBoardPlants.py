import requests
import streamlit as st
import pandas as pd
import plotly.express as px


URL = "https://cvvajx5zq0.execute-api.us-west-2.amazonaws.com/logs"
MAX_LIGTH = 750
MIN_LIGHT = 0

MAX_WATER = 300
MIN_WATER = 1023


def water_perc(value):
    return min(round((MIN_WATER - value) / (MIN_WATER - MAX_WATER) * 100, 2), 100)


def light_perc(value):
    return min(round((MIN_LIGHT - value) / (MIN_LIGHT - MAX_LIGTH) * 100, 2), 100)


def fetch(session):
    try:
        res = session.get(URL).json()
        df = pd.DataFrame.from_dict(res)
        df['light'] = df['light'].apply(light_perc)
        df['water'] = df['water'].apply(water_perc)

        return [res, df]

    except Exception:
        return [[], {}]


def calTemperature(data):
    if data and data['temperature']:
        return str(round(data['temperature'], 2)) + ' °C'
    return '0 C'


def calLight(data):
    if data and data['light']:
        return str(light_perc(data['light'])) + " %"
    return '0 %'


def calWater(data):
    if data and data['water']:
        return str(water_perc(data['water'])) + " %"
    return '0 %'


def createMarkdown(str):
    return '<p style="font-size: 30px;">' + str + '</p>'


def getLatestDate(data):
    if data and data['date']:
        return 'Ultima Actualizacion = ' + data['date'][0:10] + ' ' + data['date'][11:19]

    return 'null'


def main():
    st.title("Planta Inteligente")
    session = requests.Session()
    [data, pd] = fetch(session)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Ultimos Valores")
    with col2:
        st.text('')
    with col3:
        submitted = st.button("Actualizar")
    latest = {}
    if(len(data)):
        latest = data[len(data) - 1]

    st.caption(getLatestDate(latest), unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        txt = createMarkdown("&#127782 = " +
                             calTemperature(latest))
        st.markdown(txt, unsafe_allow_html=True)
    with col2:

        txt = createMarkdown("&#128262   = " +
                             calLight(latest))
        st.markdown(txt, unsafe_allow_html=True)
    with col3:
        txt = createMarkdown("&#128167 = " +
                             calWater(latest))
        st.markdown(txt, unsafe_allow_html=True)

    st.subheader("Historico")

    fig1 = px.line(pd, x='date', y='temperature', title='Mediciones de Temperatura',
                   labels=dict(date="Fecha", temperature="Temperatura (°C)",)
                   )
    fig1.data[0].line.color = "#00ff00"
    st.plotly_chart(fig1, use_container_width=True, sharing="streamlit")

    fig2 = px.line(pd, x='date', y='light', title='Mediciones de Luz',
                   labels=dict(date="Fecha", light="Luz (%)",)
                   )
    fig2.data[0].line.color = "#FFA500"
    st.plotly_chart(fig2, use_container_width=True, sharing="streamlit")

    fig3 = px.line(pd, x='date', y='water', title='Mediciones de Humedad',
                   labels=dict(date="Fecha", water="Humedad (%)",)
                   )
    fig3.data[0].line.color = "#009DC4"
    st.plotly_chart(fig3, use_container_width=True, sharing="streamlit")

    if submitted:
        [data, pd] = fetch(session)


if __name__ == '__main__':
    main()
