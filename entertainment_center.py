#The media file is imported so that we can create movie instances
import media
#The fresh_tomatoes file is integral for the website building process!
import fresh_tomatoes

"""
Below are 6 instances of the Movie class.
We create an instance by calling media.Movie and
adding the correct attributes for the __init__
constructor in Movie class.
"""

#Instance created for the movie: Inception
inception = media.Movie("Inception",
                        "A wanted felon can manipulate peoples' dreams",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

#Instance created for the movie: Django Unchained
django_unchained = media.Movie("Django Unchained",
                               "An African-American slave becomes a free man and seeks revenge",
                               "https://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg",
                               "https://www.youtube.com/watch?v=eUdM9vrCbow")

#Instance created for the movie: Inglorious Basterds
inglorious_basterds = media.Movie("Inglorious Basterds",
                                  "American Soldiers take down the Nazis",
                                  "https://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg",
                                  "https://www.youtube.com/watch?v=KnrRy6kSFF0")

#Instance created for the movie: Whiplash
whiplash = media.Movie("Whiplash", "A story of a drummer and its crazy teacher",
                       "https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg",
                       "https://www.youtube.com/watch?v=7d_jQycdQGo")

#Instance created for the movie: Good Will Hunting
good_will_hunting = media.Movie("Good Will Hunting",
                                "A troubled, math genius from Boston meets an important mentor",
                                "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
                                "https://www.youtube.com/watch?v=QSMvyuEeIyw")

#Instance created for the movie: Ocean's Eleven
oceans_eleven = media.Movie("Ocean's Eleven",
                            "The amazing heist of the Bellagio in Las Vegas",
                            "https://upload.wikimedia.org/wikipedia/en/6/68/Ocean%27s_Eleven_2001_Poster.jpg",
                            "https://www.youtube.com/watch?v=imm6OR605UI")

#Here we create a list for the movie instances created above
#This list makes it easier to pass these movies into a single argument
movies = [inception, django_unchained, inglorious_basterds, whiplash, good_will_hunting, oceans_eleven]

#We call the open_movies_page function from the fresh_tomatoes module
#This next line of code will create the website when we run this program
fresh_tomatoes.open_movies_page(movies)                       



