import media
import fresh_tomatoes
import imdb  # pip install imdb

ia = imdb.IMDb()
top10 = ia.get_top250_movies()[:6]
movies = []
trailers = ['https://www.youtube.com/watch?v=6hB3S9bIaco',
            'https://www.youtube.com/watch?v=sY1S34973zA',
            'https://www.youtube.com/watch?v=8PyZCU2vpi8',
            'https://www.youtube.com/watch?v=EXeTwQWrcwY',
            'https://www.youtube.com/watch?v=Dosg0p7LAB4',
            'https://www.youtube.com/watch?v=M5FpB6qDGAE']

for index, movie in enumerate(top10):
    ia.update(movie)
    movies.append(
        media.Movie(movie['long imdb title'], movie['plot outline'],
                    movie['full-size cover url'], trailers[index]))

fresh_tomatoes.open_movies_page(movies)
