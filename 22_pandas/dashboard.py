import streamlit as st
import pandas as pd
import numpy as np

url = "https://docs.google.com/spreadsheets/d/1JyrMY9ZXSusvZhiwKTLyo4i1t8VuVInJRIhMTRBmjH0/export?format=csv"
df = pd.read_csv(url)
total_students = len(df)
required_students = 50
avg_python_rating = np.round(df['Rate Yourself In Python'].mean(), 2)

st.title("Student Dashboard")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("Total Students")
        st.metric(label="Students", value=total_students, delta=(total_students - required_students) /required_students  )

with col2:
    with st.container(border=True):
        st.subheader("Avg Python Rating")
        st.metric(label="Avg", value=avg_python_rating, delta="8%")
