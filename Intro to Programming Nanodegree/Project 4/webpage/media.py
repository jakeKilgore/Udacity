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
    def __init__(self, title, description, trailer_code, poster_url):
        self.title = title
        self.description = description
        self.trailer = 'https://www.youtube.com/embed/' + trailer_code + '?controls=0&rel=0&autoplay=1'
        self.poster = poster_url

    def html(self):
        return _movie_html_template.format(poster_url=self.poster, trailer_url=self.trailer,
                                           title=self.title, description=self.description)
