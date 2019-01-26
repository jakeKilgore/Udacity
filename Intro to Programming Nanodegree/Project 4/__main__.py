import json
import os
import webbrowser

import webpage.media as media
import webpage.page as page


def main():
    movies = _get_movies_list()
    webpage = page.Webpage(movies)
    _open_webpage(webpage.html())


def _get_movies_list():
    json_file = os.path.join('webpage', 'movies.json')
    with open(json_file, 'r') as data:
        movie_data = json.load(data)
    movies = []
    for movie in movie_data:
        movies.append(media.Movie(movie['title'], movie['description'], movie['trailer_code'], movie['poster_url']))
    return movies


def _open_webpage(webpage):
    output_file = os.path.join('webpage', 'output.html')
    with open(output_file, 'w') as output:
        output.write(webpage)
    webbrowser.open(output_file)


if __name__ == "__main__":
    main()
