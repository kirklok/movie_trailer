import webbrowser


class Movie():
    """
    Class that store movie information
    for Udacity movie trailer project
    """
    def __init__(self, movie_title, movie_storyline,
                 movie_poster_image_url,
                 movie_trailer_youtube_url):
        """
        Movie class initializer that adds
        movie title, storyline, url to poster and trailer
        :param movie_title:
        :param movie_storyline:
        :param movie_poster_image_url:
        :param movie_trailer_youtube_url:
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url

    def show_trailer(self):
        """
        Method that opens browser and
        shows trailer on youtube
        :return:
        """
        webbrowser.open(self.trailer_youtube_url)
