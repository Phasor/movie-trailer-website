import media
import fresh_tomatoes    
import re

#create movie instances

trading_places = media.Movie("Trading Places",
                        "http://upload.wikimedia.org/wikipedia/en/4/4d/Trading_Places.jpg",
                        "https://www.youtube.com/watch?v=vEaXAsbvHV4",
                        "Eddie Murphy get's his own back",
                        "Eddie Murphy")
            

other_peoples_money = media.Movie("Other Peoples' Money",
                                  "http://upload.wikimedia.org/wikipedia/en/1/1a/Other_peoples_money_poster.jpg",
                                  "https://www.youtube.com/watch?v=ED95_S5-of4",
                                  "Dannie DeVito takes over the world as a banker",
                                  "Danny DeVito")

wall_street = media.Movie("Wall Street",
                          "http://upload.wikimedia.org/wikipedia/en/b/bc/Wall_Street_film.jpg",
                          "https://www.youtube.com/watch?v=7b4BcbhGggM",
                          "Michel Douglas is the King of Wall Street as Gordon Gekko",
                          "Michael Douglas and Charlie Sheen")

wolf_of_wall_street = media.Movie("The Wolf of Wall Street",
                                  "http://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",
                                  "https://www.youtube.com/watch?v=pabEtIERlic",
                                  "Di Caprio stars as the Wolf of Wall Street Jordan Belfont",
                                  "Leonardo Di Caprio")

#create list for web server

movies = [trading_places, other_peoples_money, wall_street, wolf_of_wall_street]



# run web server and serve page
fresh_tomatoes.open_movies_page(movies)

