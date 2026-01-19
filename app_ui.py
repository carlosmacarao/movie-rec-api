import streamlit as st
import requests

# Configuração da página
st.set_page_config(page_title="Recomendador de Filmes", page_icon="🎬", layout="centered")

st.title("Sistema de Recomendação de Filmes")
st.markdown("---")

st.write("Introduza o nome de um filme que gostou e eu direi o que assistir a seguir!")

movie_input = st.text_input("Nome do Filme (Ex: Central do Brasil (1998))", "")

if st.button("Obter Recomendações"):
    if movie_input:
        try:
            response = requests.get(f"http://127.0.0.1:8000/recommend/{movie_input}")
            
            if response.status_code == 200:
                data = response.json()
                recs = data['recommendations']
                
                st.success(f"Se gostou de **{movie_input}**, também poderá gostar de:")
                for i, movie in enumerate(recs, 1):
                    st.subheader(f"{i}. {movie}")
            else:
                st.error("Filme não encontrado na nossa base de dados.")
        except Exception as e:
            st.error(f"Erro ao conectar com a API: {e}")
    else:
        st.warning("Por favor, escreva o nome de um filme.")

st.markdown("---")
st.caption("Desenvolvido por Carlos Macarão")