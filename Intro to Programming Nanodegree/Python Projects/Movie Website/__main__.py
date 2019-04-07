# -*- coding: UTF-8
import json
import os
import webbrowser
from webpage import media
from webpage import page


def main():
    """Generate and open the webpage."""

    movies = _get_movies_list()
    webpage = page.Webpage(movies)
    _open_webpage(webpage.html())


def _get_movies_list():
    """Populate a list of movies from the contents of movies.json.

    Return:
        movies (list[Movie): A list of movies to be displayed on the webpage.
    """

    json_file = os.path.join('webpage', 'movies.json')
    with open(json_file, 'r') as data:
        movie_data = json.load(data)
    movies = []
    for movie in movie_data:
        movies.append(media.Movie(movie['title'], movie['description'], movie['trailer_code'], movie['poster_url']))
    return movies


def _open_webpage(webpage):
    """Write and open the webpage.

    Create or overwrite an html file to contain the page's content, then open it in a webbrowser.

    Parameters:
        webpage (string): A string of html code to be writen into a file.
    """

    output_file = os.path.join('webpage', 'output.html')
    with open(output_file, 'w') as output:
        output.write(webpage)
    webbrowser.open(output_file)


if __name__ == "__main__":
    main()
