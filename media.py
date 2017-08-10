#We need the webbrowser module to open a trailer link in a browser
import webbrowser

#Here we define what a movie is:
class Movie():
    #Documentation that explains what the Movie class does:
    """This class provides a way to store movie related information"""

    #CLASS VARIABLE:
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    #This function creates an instance with four attributes of a movie
    #The four attributes being: the title, storyline, poster, and trailer
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #INSTANCE VARIABLES:
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    #This function opens the link of the trailer of the movie that was specified
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
