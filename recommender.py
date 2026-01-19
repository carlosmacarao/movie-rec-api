import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path, encoding='utf-8')
        self.tfidf = TfidfVectorizer(stop_words='english') # Aqui vetorizamos os géneros (transformar texto em números)
        self.df['genres'] = self.df['genres'].str.replace('|', ' ')
        self.tfidf_matrix = self.tfidf.fit_transform(self.df['genres'])
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix) # Calculamos a matriz de similaridade

    def get_recommendations(self, title, top_n=3):
        
        if title not in self.df['title'].values:   # Condição para verificar se o filme existe na nossa "base de dados"
            return []

        idx = self.df.index[self.df['title'] == title][0]  # Pegar o índice do filme que corresponde ao título

        sim_scores = list(enumerate(self.cosine_sim[idx])) # Pegar as pontuações de similaridade de todos os filmes com esse filme

        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True) # Ordenar os filmes com base na similaridade (do maior para o menor)

        sim_scores = sim_scores[1:top_n+1]
        movie_indices = [i[0] for i in sim_scores]

        return self.df['title'].iloc[movie_indices].tolist()