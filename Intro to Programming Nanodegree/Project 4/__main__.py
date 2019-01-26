import json
import webbrowser
import webpage.media as media


def main():
    movies = get_movies_list()
    webpage = generate_webpage(movies)
    open_webpage(webpage)


def get_movies_list():
    with open('webpage\movies.json') as data:
        movie_data = json.load(data)
    movies = []
    for movie in movie_data:
        movies.append(media.Movie(movie['title'], movie['description'], movie['trailer'], movie['poster']))
    return movies


def generate_webpage(movies):
    movies_html = generate_movies_html(movies)
    return fill_template(movies_html)


def generate_movies_html(movies):
    movies_html = [movie.html() for movie in movies]
    return ''.join(movies_html)


def fill_template(movies_html):
    with open("webpage\mockup.html", "r") as template:
        return template.read().format(movies=movies_html)


def open_webpage(webpage):
    with open("webpage\output.html", "w") as output:
        output.write(webpage)
    webbrowser.open("webpage\output.html")


if __name__ == "__main__":
    main()
