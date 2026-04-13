import streamlit as st
import requests

st.title("Trabalho de Avaliação")

st.write("Aplicação frontend conectada ao backend.")

try:
    response = requests.get("http://backend:8000/")
    st.write("Resposta do backend:", response.json())
except Exception as e:
    st.write("Erro ao conectar ao backend:", str(e))

if st.button("Testar item"):
    try:
        response = requests.get("http://backend:8000/items/1?q=test")
        st.write("Item:", response.json())
    except Exception as e:
        st.write("Erro:", str(e))