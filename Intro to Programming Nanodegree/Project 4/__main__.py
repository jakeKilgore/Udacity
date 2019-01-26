import json
import os
import webbrowser
import webpage.media as media


def main():
    movies = _get_movies_list()
    webpage = _generate_webpage(movies)
    _open_webpage(webpage)


def _get_movies_list():
    json_file = os.path.join('webpage', 'movies.json')
    with open(json_file, 'r') as data:
        movie_data = json.load(data)
    movies = []
    for movie in movie_data:
        movies.append(media.Movie(movie['title'], movie['description'], movie['trailer'], movie['poster']))
    return movies


def _generate_webpage(movies):
    movies_html = _generate_movies_html(movies)
    return _fill_template(movies_html)


def _generate_movies_html(movies):
    movies_html = [movie.html() for movie in movies]
    return ''.join(movies_html)


def _fill_template(movies_html):
    html_file = os.path.join('webpage', 'mockup.html')
    with open(html_file, 'r') as template:
        return template.read().format(movies=movies_html)


def _open_webpage(webpage):
    output_file = os.path.join('webpage', 'output.html')
    with open(output_file, "w") as output:
        output.write(webpage)
    webbrowser.open(output_file)


if __name__ == "__main__":
    main()
