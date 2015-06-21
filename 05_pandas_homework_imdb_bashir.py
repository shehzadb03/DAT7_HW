'''
Pandas Homework with IMDB data
'''

'''
BASIC LEVEL
'''

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
movies = pd.read_table('imdb_1000.csv', sep=',', header=0)
# check the number of rows and columns
movies.shape
# check the data type of each column
movies.dtypes
# calculate the average movie duration
movies.duration.mean()
# sort the DataFrame by duration to find the shortest and longest movies
movies.sort('duration')
# create a histogram of duration, choosing an "appropriate" number of bins
movies.duration.plot(kind='hist', bins=5)
# use a box plot to display that same data
movies.duration.plot (kind='box')
'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings
movies.content_rating.value_counts()

# use a visualization to display that same data, including a title and x and y labels
movies.content_rating.value_counts().plot(kind='bar', x='Rating', y='Number of Movies', title='Movies by Content Rating')

# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP
movies.content_rating.replace(['NOT RATED', 'APPROVED', 'PASSED', 'GP'], 'UNRATED', inplace=True)

# convert the following content ratings to "NC-17": X, TV-MA
movies.content_rating.replace(['X', 'TV-MA'], 'NC-17', inplace=True)

# count the number of missing values in each column
movies.isnull().sum()

# if there are missing values: examine them, then fill them in with "reasonable" values
movies.content_rating.fillna(value='NA', inplace=True)
# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours

movies[movies.duration >= 120].star_rating.mean()

movies[movies.duration <= 120].star_rating.mean()

# use a visualization to detect whether there is a relationship between star rating and duration

movies.plot(kind='scatter', x='star_rating', y='duration')

# calculate the average duration for each genre

movies.groupby('genre').duration.mean()

'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration

movies.plot(kind='scatter', x='duration', y='content_rating') #not sure why this isn't working

# determine the top rated movie (by star rating) for each genre

movies.sort('star_rating', ascending=False).groupby('genre')# Able to sort but unable to group by genre

# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates

movies.title.duplicated().value_counts() ## identified 4 duplicate movie titles
movies.duplicated().value_counts() ## verifies there are no duplicate rows
movies[movies.duplicated()] ## checked to see if there were any rows that were duplicated but nothign shows


# calculate the average star rating for each genre, but only include genres with at least 10 movies

movies[movies.genre.index >= 10].groupby('genre').star_rating.mean()


'''
BONUS
'''

# Figure out something "interesting" using the actors data!
