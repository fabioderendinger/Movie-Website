$(document).ready(function(){

    var trailer_url;

    // Identify the active tile in the carousel and display it's movie metadata in the preview-container
    $('.carousel').carousel({
        onCycleTo: function (ele, dragged) {
            
            // Variables definition
            // Get movie metadata for the active tile in the carousel
            var title = $(ele).attr('data-movie-title');
            var storyline = $(ele).attr('data-storyline');
            var wallpaper_url = $(ele).attr('data-wallpaper');
            var trailer_id = $(ele).attr('data-trailer-youtube-id');
            trailer_url = 'https://www.youtube.com/embed/' + trailer_id + '?autoplay=1&html5=1&VQ=HD720&iv_load_policy=3';
            var director = $(ele).attr('data-director');
            var country = $(ele).attr('data-country');
            var rating = $(ele).attr('data-rating');

            // Generate HTML containing the movie metadata
            $('.preview-container').html(
                `<img class ="movie-wallpaper" src=` + wallpaper_url + ` alt="">
                <div class="overlay">
                    <div class="container">
                        <div class="row">
                            <div class="col l12 xl7">
                                <h2 class="movie-title"><b>` + title + `</b></h1>
                                <p class="storyline">` + storyline + `</p>
                                <table>
                                    <tbody>
                                    <tr>
                                    <td>Directed by</td>
                                    <td>` + director + `</td>
                                    </tr>
                                    <tr>
                                    <td>Country</td>
                                    <td>` + country + `</td>
                                    </tr>
                                    <tr>
                                    <td>IMDB Rating</td>
                                    <td>` + rating + `</td>
                                    </tbody>
                                </table>
                                <a class="waves-effect waves-light btn modal-trigger" href="#modal1">Watch Trailer</a>
                            </div>
                        </div>
                    </div>
                </div>`
            );
        }
    });


    // the "href" attribute of the modal trigger must specify the modal ID that wants to be triggered
    $('.modal').modal({
        dismissible: true, // Modal can be dismissed by clicking outside of the modal
        opacity: .5, // Opacity of modal background
        inDuration: 300, // Transition in duration
        outDuration: 200, // Transition out duration
        startingTop: '4%', // Starting top style attribute
        endingTop: '10%', // Ending top style attribute
        ready: function(modal, trigger) { // Callback for Modal open. Modal and trigger parameters available.
            // Start video when modal is opened
            $('.video-container').html(
                '<iframe src=' + trailer_url + ' frameborder="0" allowfullscreen></iframe>'
            );
        },
        complete: function() {
            // Stop video when modal is closed
            $('.video-container').empty();
        }
    });

});