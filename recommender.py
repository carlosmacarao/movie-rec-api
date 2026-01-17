import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, csv_path):
        # 1. Carregar os dados
        self.df = pd.read_csv(csv_path, encoding='utf-8')
        # 2. Vetorizar os géneros (transformar texto em números)
        self.tfidf = TfidfVectorizer(stop_words='english')
        # Substituímos as barras por espaços para o TF-IDF funcionar melhor
        self.df['genres'] = self.df['genres'].str.replace('|', ' ')
        self.tfidf_matrix = self.tfidf.fit_transform(self.df['genres'])
        # 3. Calcular a matriz de similaridade
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

    def get_recommendations(self, title, top_n=3):
        # Verificar se o filme existe no nosso "banco de dados"
        if title not in self.df['title'].values:
            return []

        # Pegar o índice do filme que corresponde ao título
        idx = self.df.index[self.df['title'] == title][0]

        # Pegar as pontuações de similaridade de todos os filmes com esse filme
        sim_scores = list(enumerate(self.cosine_sim[idx]))

        # Ordenar os filmes com base na similaridade (do maior para o menor)
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Pegar os índices dos filmes mais similares (excluindo o próprio filme)
        sim_scores = sim_scores[1:top_n+1]
        movie_indices = [i[0] for i in sim_scores]

        # Retornar os títulos dos filmes recomendados
        return self.df['title'].iloc[movie_indices].tolist()