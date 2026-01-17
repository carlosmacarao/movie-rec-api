# Movie Recommendation System API
Este projeto é um sistema de recomendação de filmes "End-to-End" que utiliza Processamento de Linguagem Natural (NLP) e similaridade matemática para sugerir conteúdos baseados no perfil de géneros.

## Tecnologias Utilizadas


**Backend** - FastAPI <br>
**Frontend** - Streamlit - Para Interface de usuário <br>
**Data Science** - Pandas / Scikit-learn - Manipulação de dados e cálculo de similaridade. <br>
**Algoritmo** - Cosine Similarity - Cálculo de proximidade entre vetores de filmes. 

## Como funciona?

O sistema utiliza a técnica de **Filtragem Baseada em Conteúdo**. 
1. Os géneros dos filmes são convertidos em matrizes numéricas usando **TF-IDF**.
2. Calculamos o ângulo entre os vetores de cada filme através da **Similaridade de Cosseno**.
3. A API devolve os filmes com menor distância angular (mais semelhantes) ao filme pesquisado.

## Como Executar o Projeto
Instale as dependências:
1. Numpy
2. Pandas
3. Streamlit

Iniciar o Servidor (Backend):
uvicorn main:app --reload

Iniciar a Interface (Frontend):
streamlit run app_ui.py
