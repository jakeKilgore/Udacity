import webbrowser
import classes.media as media
poster_html = '''
<div class="poster-container">
    <img class="poster" 
        src="{poster-url}"
        data-trailer="{trailer-url}"
        data-title="{title}"
        data-description="{description}"
    >
</div>
<h2 class="poster-title">{title}</h2>
            '''

def main():
    open_webpage()


def open_webpage():
    movie = media.Movie("", "", "", "")
    webbrowser.open("mockup.html")


if __name__ == "__main__":
    main()
