import fresh_tomatoes
import media

north_by_northwest = media.Movie("North by Northwest", "A man fights a case of mistaken identity.",
                                 "https://upload.wikimedia.org/wikipedia/commons/8/83/Northbynorthwest1.jpg"
                                 "https://www.youtube.com/watch?v=qk0GbTMMbP0")

fight_club = media.Movie("Fight Club", "Mischief, Mayhem, Soap.",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

oceans_11 = media.Movie("Ocean's 11", "11 con men take on a Las Vegas casino.",
                        "https://upload.wikimedia.org/wikipedia/en/6/68/Ocean%27s_Eleven_2001_Poster.jpg",
                        "https://www.youtube.com/watch?v=imm6OR605UI")

the_prestige = media.Movie("The Prestige", "Two rival magicians compete in Victorian-era London.",
                           "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
                           "https://www.youtube.com/watch?v=JucYLWfFiAs")

hail_caesar = media.Movie("Hail, Caesar!", "Cohen brothers comedy set in Hollywood's Golden Age.",
                          "https://upload.wikimedia.org/wikipedia/en/a/a9/Hail%2C_Caesar%21_poster.png",
                          "https://www.youtube.com/watch?v=kMqeoW3XRa0")

jurassic_park = media.Movie("Jurassic Park", "An adventure 65 million years in the making",
                            "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",
                            "https://www.youtube.com/watch?v=lc0UehYemQA")

movies = [north_by_northwest, fight_club, oceans_11, the_prestige, hail_caesar, jurassic_park]
fresh_tomatoes.open_movies_page(movies)
