# -*- coding: UTF-8
_movie_html_template = '''
        <div class="movie">
            <div class="poster-container">
                <img class="poster" 
                    src="{poster_url}"
                    alt="Movie poster for {title}"
                    data-trailer="{trailer_url}"
                    data-title="{title}"
                    data-description="{description}"
                />
            </div>
            <h2 class="poster-title">{title}</h2>
        </div>
'''


class Movie:
    """Class for defining movies.

    Attributes:
        title (string): Title of the movie.
        description (string): Description of the movie.
        trailer (string): URL to embed the trailer.
        poster (string): URL for the poster image.
    """

    def __init__(self, title, description, trailer_code, poster_url):
        """Constructor for the movie class.

        Parameters:
            title (string): Title of the movie.
            description (string): Description of the movie.
            trailer_code (string): Youtube trailer code.
            poster_url (string): URL for the poster image.
        """

        self.title = title
        self.description = description
        self.trailer = 'https://www.youtube.com/embed/' + trailer_code + '?controls=0&rel=0&autoplay=1'
        self.poster = poster_url

    def html(self):
        """Represent the movie as HTML code.

        Return:
            string: HTML code representing the movie.
        """

        return _movie_html_template.format(poster_url=self.poster, trailer_url=self.trailer,
                                           title=self.title, description=self.description)
