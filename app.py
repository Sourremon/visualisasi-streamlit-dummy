import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="Visualisasi Interaktif", layout="wide")

# --- Header (image, title, description) ---
from pathlib import Path

# Prefer local image if available, otherwise fall back to web image

st.title("Visualisasi Data Interaktif — 5 Pilihan Grafik")
st.write("Aplikasi demo sederhana yang menampilkan 5 jenis visualisasi (pie, area, bar, line, map) menggunakan dataset contoh berukuran 10 baris.")

# --- Create a sample dataset (10 rows) ---
np.random.seed(42)
categories = [f"Kategori {i+1}" for i in range(5)]
values = np.random.randint(10, 100, size=10)
# create 10 rows with categories assigned
data = {
    "id": list(range(1, 11)),
    "name": [f"Item {i+1}" for i in range(10)],
    "category": [np.random.choice(categories) for _ in range(10)],
    "value": values,
    "date": [datetime.today() - timedelta(days=i*3) for i in range(10)],
    # random coordinates centered around Jakarta (lat ~ -6.2, lon ~ 106.8) for the map demo
    "lat": -6.2 + np.random.normal(scale=0.05, size=10),
    "lon": 106.8 + np.random.normal(scale=0.05, size=10),
}

df = pd.DataFrame(data)

# --- Sidebar controls ---
chart_type = st.sidebar.selectbox("Pilih jenis visualisasi:", [
    "Pie Chart",
    "Area Chart",
    "Bar Chart",
    "Line Chart",
    "Map",
])

show_table = st.sidebar.checkbox("Tampilkan tabel data", value=True)

# --- Layout ---
st.header(f"{chart_type}")

# --- Render chosen chart ---
if chart_type == "Pie Chart":
    # aggregate by category
    pie_df = df.groupby("category")[["value"]].sum().reset_index()
    fig = px.pie(pie_df, names='category', values='value', title='Proporsi Nilai per Kategori')
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Area Chart":
    # area chart over time
    area_df = df.sort_values('date').groupby('date', as_index=False).sum()
    fig = px.area(area_df, x='date', y='value', title='Area: Perubahan Total Nilai per Tanggal')
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Bar Chart":
    fig = px.bar(df, x='name', y='value', color='category', title='Bar Chart: Value per Item')
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Line Chart":
    # line chart of each category across time (we'll pivot)
    tmp = df.copy()
    tmp['date_str'] = tmp['date'].dt.strftime('%Y-%m-%d')
    pivot = tmp.pivot_table(index='date_str', columns='category', values='value', aggfunc='sum').fillna(0)
    fig = px.line(pivot, x=pivot.index, y=pivot.columns, title='Line Chart: Value per Category over Time')
    fig.update_layout(xaxis_title='Date')
    st.plotly_chart(fig, use_container_width=True)

else:  # Map
    st.write("Menampilkan lokasi 10 item pada peta (koordinat acak di sekitar Jakarta).")
    st.map(df[['lat', 'lon']].rename(columns={'lat':'latitude','lon':'longitude'}), zoom=11)

# --- Show data and download ---
if show_table:
    st.subheader("Tabel data (10 baris)")
    st.dataframe(df)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "data_10_rows.csv", "text/csv")

# Footer / Additional description
st.markdown("---")
st.markdown("**Deskripsi :** Data dibuat secara acak untuk demonstrasi. Setiap `Item` memiliki `category`, `value`, `date`, dan koordinat (`lat`, `lon`) untuk contoh peta.")
