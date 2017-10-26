import media
import fresh_tomatoes

# create movie objects of favorite movies
in_bruges = media.Movie("In Bruges", 
                        "Guilt-stricken after a job gone wrong, hitman Ray and his partner await orders from their ruthless boss in Bruges, Belgium, the last place in the world Ray wants to be.", 
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BZGQ5YWU5OGMtMTU2Ni00NmJhLWEwNzItMGMxMmRjMDI3MTQxXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://images5.alphacoders.com/342/342202.jpg", 
                        "https://www.youtube.com/watch?v=p-gG2qo_l_A",
                        "Martin McDonagh",
                        "UK",
                        "7.9")

three_idiots = media.Movie("Three Idiots", 
                        "Two friends are searching for their long lost companion. They revisit their college days and recall the memories of their friend who inspired them to think differently, even as the rest of the world called them &quot;idiots&quot;.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BZWRlNDdkNzItMzhlZC00YTdmLWIwNjktYjY5NjQ1ZmQ3N2FkXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UY268_CR9,0,182,268_AL_.jpg",
                        "http://media.glamsham.com/download/wallpaper/movies/images/3/3idiot-33-12x9.jpg", 
                        "https://www.youtube.com/watch?v=K0eDlFX9GMc",
                        "Rajkumar Hirani",
                        "India",
                        "8.4")

lucky_number_slevin = media.Movie("Lucky Number Slevin", 
                        "A case of mistaken identity lands Slevin into the middle of a war being plotted by two of the city's most rival crime bosses: The Rabbi and The Boss. Slevin is under constant surveillance by relentless Detective Brikowski as well as the infamous assassin Goodkat and finds himself having to hatch his own ingenious plot to get them before they get him.",
                        "https://i.pinimg.com/originals/49/41/8e/49418e15171b48a2d5166443980ca548.jpg",
                        "https://images4.alphacoders.com/217/217226.jpg", 
                        "https://www.youtube.com/watch?v=fVIUEcizkPc",
                        "Paul McGuigan",
                        "USA",
                        "7.8")

shutter_island = media.Movie("Shutter Island", 
                        'In 1954, a U.S. Marshal investigates the disappearance of a murderer, who escaped from a hospital for the criminally insane.',
                        "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
                        "https://images4.alphacoders.com/983/98324.jpg", 
                        "https://www.youtube.com/watch?v=5iaYLCiq5RM",
                        "Martin Scorsese",
                        "USA",
                        "8.1")

lord_of_the_rings = media.Movie("The Lord of the Rings: The Return of the King", 
                        "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
                        "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
                        "https://images3.alphacoders.com/161/thumb-1920-161237.jpg", 
                        "https://www.youtube.com/watch?v=r5X-hFf6Bwo",
                        "Peter Jackson",
                        "USA",
                        "8.9")

# generate and open html page of favorite movies
movies = [in_bruges, three_idiots, lucky_number_slevin, shutter_island, lord_of_the_rings]
fresh_tomatoes.open_movies_page(movies)