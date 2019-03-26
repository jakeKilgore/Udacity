# -*- coding: UTF-8
import os


class Webpage:
    """Class for handling constructing the webpage

    Attributes:
        movies (list[Movie): A list of movies to be displayed on the webpage.
    """

    def __init__(self, movies):
        """Constructor for the Webpage class.

        Parameters:
            movies (list[Movie): A list of movies to be displayed on the webpage.
        """

        self.movies = movies

    def html(self):
        """Generate a string of HTML for the webpage

        Return:
            string: HTML code string for the entire webpage.
        """

        movies_html = self._generate_movies_html()
        html_file = os.path.join('webpage', 'mockup.html')
        with open(html_file, 'r') as template:
            return template.read().format(movies=movies_html)

    def _generate_movies_html(self):
        """Generate a list of HTML strings from the list of movies

        Return:
            list[String]: HTML strings for each movie.
        """

        movies_html = [movie.html() for movie in self.movies]
        return ''.join(movies_html)
