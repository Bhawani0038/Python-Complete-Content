import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Business Dashboard", layout="wide")

df = pd.read_csv("loan_approval_dataset_200_rows.csv")
goals = {
    "estimated_application" : 250,
    "total_loan_distribution_estimation" : 80000000
}
kpi = {
    "total_applicants" : df['applicant_id'].count(),
    "total_loan_distributed" : df[df['loan_approved'] == 1]["loan_amount_inr"].sum(),
    "total_loan_pass" : df[df['loan_approved'] == 1]["applicant_id"].count(),
    "avg cibil score" : df["cibil_score"].mean()

}

people_count = df.groupby(by = 'employment_type').agg(
    total_applicant = ("applicant_id", "count")
).reset_index()



application_completion_rate = ( kpi["total_applicants"] - goals["estimated_application"]) / goals["estimated_application"]
st.title("Business Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    with st.container(border=True):
        st.caption("Total Applicant")
        st.metric("Applicant", kpi["total_applicants"], application_completion_rate )

with col2:
    with st.container(border=True):
        st.caption("Total Loans Given")
        st.metric("Loan", kpi["total_loan_distributed"], "+8.2%")

with col3:
    with st.container(border=True):
        st.caption("Loan passed count")
        st.metric("passed", kpi["total_loan_pass"], "+5.4%")

with col4:
    with st.container(border=True):
        st.caption("Cibil Score")
        st.metric("Avg", kpi["avg cibil score"], "-2.1%")



st.subheader("Sales by Month")
st.bar_chart(people_count, x ="employment_type", y = "total_applicant")
