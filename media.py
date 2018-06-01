# imports webbrowser module
import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    """defines init function, creates memory space for new
    instance of class Movie"""
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    """launches web browser to view movie trailer"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
