import streamlit as st

import pandas as pd

# Load the budget data

budget_data = pd.read_csv("church_budget.csv")

# Streamlit app

st.title("Church Budget Tracker")

# Input form for adding expenses

st.subheader("Add Expenses")

expense_category = st.text_input("Category")

expense_amount = st.number_input("Amount", step=0.01, format="%.2f")

if st.button("Add Expense"):

    budget_data = budget_data.append({"Category": expense_category, "Expenses": expense_amount}, ignore_index=True)

    st.success("Expense added successfully!")

# Input form for adding income

st.subheader("Add Income")

income_category = st.text_input("Category")

income_amount = st.number_input("Amount", step=0.01, format="%.2f")

if st.button("Add Income"):

    budget_data = budget_data.append({"Category": income_category, "Income": income_amount}, ignore_index=True)

    st.success("Income added successfully!")

# Display the budget data

st.subheader("Budget Overview")

st.dataframe(budget_data)

# Calculate total income and expenses

total_income = budget_data["Income"].sum()

total_expenses = budget_data["Expenses"].sum()

# Display total income and expenses

st.subheader("Financial Summary")

st.write("Total Income:", total_income)

st.write("Total Expenses:", total_expenses)

# Calculate net income

net_income = total_income - total_expenses

# Display net income

st.write("Net Income:", net_income)

# Display expense breakdown

st.subheader("Expense Breakdown")

expense_breakdown = budget_data.groupby("Category")["Expenses"].sum()

st.bar_chart(expense_breakdown)
