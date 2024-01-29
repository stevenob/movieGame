import requests
import random
import time
import os

apiKey = "81c8b8b8"
url = f"https://www.omdbapi.com/?y=2023&apikey={apiKey}"

def getMovie(movie):
    movie = movie.strip()
    movie = movie.replace(' ','+')
    x = requests.get(f"http://www.omdbapi.com/?t={movie}&apikey={apiKey}")
    return x.json()

os.system('cls')
print("*****")
# Readling list of movies
movie_list = open("movies.txt", "r") 
data = movie_list.read() 
movies = data.split("\n") 
movie_list.close() 
print("Pulling from list of Academy Award winning movies...")
time.sleep(1)

# Setting random movie from list
randInt = random.randrange(32)
movie = movies[randInt]
print("Choosing movie...")
time.sleep(2.5)

print("Starting Game!")
time.sleep(1)
# creating game loop
game = True
guess = 0
hidden_word = ""
mi = getMovie(movie)

for m in movie:
        if m == ' ':
            hidden_word += (' ')
        else:
            hidden_word += ('_')

while game:
    os.system('cls')
    print(hidden_word)
    if guess == 0:
         print(f"Year: {mi['Year']}")
    elif guess == 1:
         print(f"Year: {mi['Year']}\nDirector: {mi['Director']}")
    elif guess == 2:
         print(f"Year: {mi['Year']}\nDirector: {mi['Director']}\nGenre: {mi['Genre']}")
    elif guess == 3:
         print(f"Year: {mi['Year']}\nDirector: {mi['Director']}\nGenre: {mi['Genre']}\nActors: {mi['Actors']}")
    elif guess == 4:
         print(f"Year: {mi['Year']}\nDirector: {mi['Director']}\nGenre: {mi['Genre']}\nActors: {mi['Actors']}\nPlot: {mi['Plot']}")
    else:
         print(f"The movie was: {mi['Title']}")
         game = False
    ans = input()
    if ans.strip() == movie.lower():
        print('Winner!')
        game = False
    else:
        guess += 1    
