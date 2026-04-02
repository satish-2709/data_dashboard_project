import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("data/sales_data.csv")

st.set_page_config(layout="wide")  # IMPORTANT 🔥

st.title("📊 Sales Dashboard")

# =========================
# KPIs (Top row)
# =========================
col1, col2, col3 = st.columns(3)

total_sales = df["Sales"].sum()
total_orders = len(df)
top_person = df.groupby("Name")["Sales"].sum().idxmax()

col1.metric("💰 Total Sales", total_sales)
col2.metric("📦 Total Orders", total_orders)
col3.metric("🏆 Top Performer", top_person)

# =========================
# Charts row
# =========================
col4, col5 = st.columns(2)

# Sales by Person
summary = df.groupby("Name")["Sales"].sum().reset_index()
col4.subheader("Sales by Person")
col4.bar_chart(summary.set_index("Name"))

# Sales by Product
product_summary = df.groupby("Product")["Sales"].sum().reset_index()
col5.subheader("Sales by Product")
col5.bar_chart(product_summary.set_index("Product"))

# =========================
# Filter + Table
# =========================
col6, col7 = st.columns([1,2])

person = col6.selectbox("Select Person", df["Name"].unique())

filtered_df = df[df["Name"] == person]

col7.subheader("Filtered Data")
col7.write(filtered_df)