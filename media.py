
import webbrowser

class Movie():
    """This class stores the data for each movie"""
    
    def __init__(self, movie_title, movie_image_url, movie_youtube_url, movie_storyline, main_actor_names):
        self.title = movie_title
        self.trailer_youtube_url = movie_youtube_url
        self.poster_image_url = movie_image_url
        self.storyline = movie_storyline
        self.actors = main_actor_names

    




