import streamlit as st
import pandas as pd
import duckdb

st.write("""
# SQL SRS
Spaced Repetition System SQL practice
""")

option = st.selectbox(
    'What would you like to review?',
    ('Joins', 'GroupBy', 'Windows Functions'),
    index=None,
    placeholder="Select a theme...",
)

st.write('You selected:', option)

data = {"Nom": ["Capelle", "Zamboni", "Charly"],
        "Prénom": ["David", "Sabine", "Steven"],
        "Salaire moyen": [4000, 1300, 1600]}
df = pd.DataFrame(data)

tab1, tab2 = st.tabs(["Onglet 1", "Onglet 2"])

with tab1:
    sql_query = st.text_area(label="Entrez votre input")
    result = duckdb.sql(sql_query).df()
    st.write(f"Vous avez entré la requête suivante:{sql_query}")
    st.dataframe(result)
