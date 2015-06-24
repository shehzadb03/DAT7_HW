

import requests
import pandas as pd

# define a function that accepts an IMDb ID and returns a dictionary of movie information
def get_movie_info(id):
    r = requests.get('http://www.omdbapi.com/?i=' + id + '&plot=short&r=json')
    info = r.json()
    if info['Response']=='True':
        return info.text
    else:
        return None

# test the function
 
get_movie_info('tt0416449')

# open the file of IDs (one ID per row), and store the IDs in a list
 
movies = pd.read_csv('imdb_ids.txt', header=None)
ids = []
 
for i in movies:
    ids.append(movies)
 

# get the information for each movie, and store the results in a list
 
results = []
for i in ids:
     results.append(get_movie_info(i))
     
# check that the list of IDs and list of movies are the same length
assert(len(ids) == len(results))
 
# convert the list of movies into a DataFrame
 
Df = DataFrame('movies')