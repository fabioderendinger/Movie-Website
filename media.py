import webbrowser

class Movie():

    def __init__(self, movie_title, movie_storyline, poster_image_url, wallpaper_url, trailer_youtube_url, movie_director, movie_country, imdb_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.wallpaper_url = wallpaper_url
        self.trailer_youtube_url = trailer_youtube_url
        self.director = movie_director
        self.country = movie_country
        self.rating = imdb_rating

    def show_trailer(self):
        webbrowser.open_new(self.url)
