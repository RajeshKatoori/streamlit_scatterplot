import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

User_name = st.text_input("Enter user name")

file_upload=st.file_uploader("choose a file")

button = st.button("Submmit")
if button:

    dataframe = pd.read_csv(file_upload)
    st.write(dataframe.head())

    fig=plt.figure()
    plt.scatter(dataframe["sepal.length"],dataframe["petal.length"])
    plt.xlabel("petal.length")
    plt.ylabel("sepal.length")

    st.write(fig)
