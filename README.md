# Movie Trailer Website
This .zip file contains Python files which generate a static webpage that presents movies with their respective posters and trailers.

## Getting Started
Download the .zip file, which has:
* media.py
* entertainment_center.py
* fresh_tomatoes
* README.md

Open each file to examine its contents and comments in the code.

### media.py
This file contains the __Movie__ class and its __ init__ and __show_trailer__ functions.




The __init__ function creates an instance of a specific movie. It takes four attributes:
* Title
* Storyline
* Movie Poster
* Movie Trailer

The __show_trailer__ function opens the YouTube link of the movie that was specified in the argument. It is important to note that the module __webbroswer__ was imported in order to be able to use this function.


### entertainment_center.py
This file contains six instances of movies created with __media.Movie()__ by adding the correct attributes needed for the __init__ constructor from the __Movie__ class.

The six movies chosen for this website are:
* Inception
* Django Unchained
* Inglorious Basterds
* Whiplash
* Good Will Hunting
* Ocean's Eleven

In addition, the __fresh_tomatoes__ module was imported so that function __open_movies_page()__ is available for use.

## Running the Program
In order to test and view the website, we must run the __entertainment_center.py__ module. The line of code that will create the website is:

```
fresh_tomatoes.open_movies_page(movies)
```
The argument, movies, is a list of the created instances.

## Built With
* [IDLE](https://docs.python.org/2/library/idle.html) -  an integrated development environment for Python
* [Atom](https://atom.io) - Text editor used to create this README

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors
* **Chris Jeon**

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* Kunal from Udacity
