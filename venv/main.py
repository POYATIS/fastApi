from fastapi import FastAPI
from fastapi import Request
from pydantic import BaseModel


app = FastAPI()
app.title = "Fast"
app.version = "1.0"

class Movie(BaseModel):
    id:int
    title:str
    overview:str
    year:int
    rating:int
    category:str

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]


@app.get("/", tags=["Home"])
def menssage():
    return "holaaa"

@app.get("/movies", tags=["movies"])
def get_movies():
    return movies

@app.get(path="/movies/{id}", tags=["movie"], summary="Show a movie in the app")
def get_all_movies(id: int):
    """Get a movie
    - Params:
        id: int
    - Returns a json with de basic movie information
        id: int
        title: str
        overview: str
        year: int
        rating: int
        category: str
        
    """
    movie = [movie for movie in movies if movie['id'] == id]
    if not movie:
        return {'error': 'Movie not found' }
    return movie


@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str, year: int):
    #return category + " " + str(year)
    return [movie for movie in movies if movie['category'] == category]

@app.post('/movies/', tags=['movies'])
def add_movie(movie: Movie):
    movie.append(movie)
    return movie

@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
     for index, item in enumerate(movies):
        if item["id"] == id:
            movies[index].update(movie)
            movies[index]["id"] = id
            return movies[index]
