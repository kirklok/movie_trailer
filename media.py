import webbrowser


class Movie():
    # Movie class constructor that adds
    # movie title, storyline, url to poster and trailer
    def __init__(self, movie_title, movie_storyline,
                 movie_poster_image_url,
                 movie_trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url

    # Movie class method that opens trailer on youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
