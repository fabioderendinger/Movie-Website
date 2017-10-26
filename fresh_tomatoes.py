import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!--Import Google Icon Font-->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <!--Import materialize.css-->
    <link type="text/css" rel="stylesheet" href="css/materialize.min.css"  media="screen,projection"/>
    <!--Import style.css-->
    <link rel="stylesheet" type="text/css" href="css/style.css">

    <!--Import jQuery before materialize.js-->
    <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="js/materialize.min.js"></script>

    <!--Import custom JS functions.js-->
    <script src="js/functions.js"></script>

    <script type="text/javascript" charset="utf-8">
    </script>

</head>
'''


# The main page layout
main_page_content = '''
  <body>

    <!-- Trailer Video Modal -->
    <div id="modal1" class="modal">
        <div class="modal-content">
            <div class="video-container">
            </div>
        </div>
    </div>

    <!-- Main Page Content -->
    <div class="preview-container">
    </div>
    <div class="list-container">
        <div class="carousel">
            {movie_tiles}
        </div>
    </div>
'''


# A single movie entry html template
movie_tile_content = '''
<a class="carousel-item" href="#one!" data-movie-title="{movie_title}" data-storyline="{movie_storyline}" data-wallpaper="{wallpaper_url}" data-trailer-youtube-id="{trailer_youtube_id}" data-director="{movie_director}" data-country="{movie_country}" data-rating="{movie_rating}"><img src="{poster_image_url}"></a>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            wallpaper_url=movie.wallpaper_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_director=movie.director,
            movie_country=movie.country,
            movie_rating=movie.rating
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
