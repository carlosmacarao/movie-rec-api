from fastapi import FastAPI, HTTPException
from recommender import MovieRecommender

app = FastAPI(title="Movie Rec API", description="API de Recomendação de Filmes do Carlos")

# Inicializamos o motor de recomendação
recommender = MovieRecommender('movies.csv')

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Recomendação! Use o endpoint /recommend/{titulo}"}

@app.get("/recommend/{movie_title}")
def recommend(movie_title: str):
    recommendations = recommender.get_recommendations(movie_title)
    
    if not recommendations:
        raise HTTPException(status_code=404, detail="Filme não encontrado ou sem recomendações.")
    
    return {
        "movie_searched": movie_title,
        "recommendations": recommendations
    }