import os


def _fill_template(movies_html):
    html_file = os.path.join('webpage', 'mockup.html')
    with open(html_file, 'r') as template:
        return template.read().format(movies=movies_html)


class Webpage:
    def __init__(self, movies):
        self.movies = movies

    def html(self):
        movies_html = self._generate_movies_html()
        return _fill_template(movies_html)

    def _generate_movies_html(self):
        movies_html = [movie.html() for movie in self.movies]
        return ''.join(movies_html)
