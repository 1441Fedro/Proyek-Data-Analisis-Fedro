import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

all_df = pd.read_csv("all_data.csv")

def filter_data_by_city(df, city):
    filtered_df = all_df[all_df["station"] == city]
    return filtered_df

with st.sidebar:
    st.sidebar.title("Tentang Saya")

    st.sidebar.subheader("Nama")
    st.sidebar.write("Fedro Maulana Jatmika")

    st.sidebar.subheader("Email")
    st.sidebar.write("jatmikafedro@gmail.com")

    st.sidebar.subheader("ID Dicoding")
    st.sidebar.write("fedro_mj")
    
st.header("Proyek Akhir Dicoding")
tab1, tab2, tab3 = st.tabs(["Data Frame", "Question 1", "Question 2"])

with tab1:
    st.header("Data Yang Digunakan Pada Proyek Akhir Dicoding")
    st.dataframe(data=all_df, width=550, height=400)

with tab2:
    st.header("Rata-rata Tahunan Jumlah NO2 di Setiap Kota")
    question1_df = all_df.groupby(by=["station"]).agg({
        "NO2_mean": "mean"
    }).sort_values(by="NO2_mean", ascending=False)

    question1_df.rename(columns={
        "NO2_mean": "Rata-rata Tahunan"
    }, inplace=True)

    st.dataframe(data=question1_df, width=400, height=300)
    st.bar_chart(data=question1_df)

with tab3:
    selected_city = st.selectbox("Pilih kota:", all_df["station"].unique(),
                                index=None, placeholder="Silahkan pilih kota...")

    filtered_df = filter_data_by_city(all_df, selected_city)

    filtered_df = filtered_df.groupby(by=["year"]).agg({
        "NO2_sum": "sum"
    })

    filtered_df.rename(columns={
        "NO2_sum": "Jumlah Tahunan"
    }, inplace=True)

    st.dataframe(data=filtered_df, width=400, height=200)

    st.bar_chart(data=filtered_df["Jumlah Tahunan"])
