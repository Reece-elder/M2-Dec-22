# Movie - Directors Dictionary
# Directors as keys, and value is movies
# Instead we want value as a List of movies

director_movies = {"Tarantino" : ["reservoir dogs", "Django Unchained", "Kill Bill", "Pulp Fiction"], "George Lucas" : ["Starwars Episode 4", "THX"], "Steven Spielberg" : "Jaws"}
print(director_movies)
print(director_movies["Tarantino"])
print(director_movies["Steven Spielberg"])

choice = input("Please enter Directors name: ")
print(director_movies[choice])