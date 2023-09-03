import streamlit as st
import plotly.express as px
import sqlite3


data_bass = sqlite3.connect("databass.db")


def read():
    file = data_bass.cursor()
    data = file.execute("SELECT *FROM events ")
    data = data.fetchall()
    return data


d = read()
temp = []
date = []
for b in d:
    temp.append(b[0])
    date.append(b[1])
print(temp, date)

nem = {"x": "date", "y": "temperature"}
figure = px.line(x=date, y=temp, labels=nem)
st.plotly_chart(figure)
