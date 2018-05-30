import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar = media.Movie("Avatar", "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4")
#print(avatar.storyline)
#avatar.show_trailer()
fight_club = media.Movie("Fight Club", "Mischief, Mayhem, Soap.",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")
#fight_club.show_trailer()
oceans_11 = media.Movie("Ocean's 11", "11 con men take on a Las Vegas casino.",
                        "https://upload.wikimedia.org/wikipedia/en/6/68/Ocean%27s_Eleven_2001_Poster.jpg",
                        "https://www.youtube.com/watch?v=imm6OR605UI")

the_prestige = media.Movie("The Prestige", "Two rival magicians compete in Victorian-era London.",
                           "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
                           "https://www.youtube.com/watch?v=JucYLWfFiAs")

hail_caesar = media.Movie("Hail, Caesar!", "Cohen brothers comedy set in Hollywood's Golden Age.",
                          "https://upload.wikimedia.org/wikipedia/en/a/a9/Hail%2C_Caesar%21_poster.png",
                          "https://www.youtube.com/watch?v=kMqeoW3XRa0")

movies = [toy_story, avatar, fight_club, oceans_11, the_prestige, hail_caesar]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)

#north_by_northwest = media.Movie("North by Northwest", "A man fights a case of mistaken identity.",
                                 #"https://upload.wikimedia.org/wikipedia/commons/8/83/Northbynorthwest1.jpg"
                                 #"https://www.youtube.com/watch?v=qk0GbTMMbP0")

#jurassic_park = media.Movie("Jurassic Park", "An adventure 65 million years in the making",
                            #"https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",
                            #"https://www.youtube.com/watch?v=lc0UehYemQA")

