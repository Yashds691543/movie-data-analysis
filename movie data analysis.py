import pandas

# Load individual tables
users = pandas.read_csv('/Users/yashds/Downloads/movielens/users.csv')
ratings = pandas.read_csv('/Users/yashds/Downloads/movielens/ratings.csv')
movies = pandas.read_csv('/Users/yashds/Downloads/movielens/movies.csv')

# Merge tables
mr = pandas.merge(users, ratings)
data = pandas.merge(movies, mr)

df = data.groupby(['genres'])['rating'].mean().sort_values(ascending=False)[0:10]
df

genres_counts = data.groupby('genres')['rating'].count()
popular_genres = genres_counts[genres_counts >= 5000].index
popular_genres.columns = ['rating', 'num_ratings']
genre_avg_ratings = data[data['genres'].isin(popular_genres)].groupby('genres')['rating'].mean()
top_5_genres = genre_avg_ratings.sort_values(ascending=False)[0:5]
top_5_genres

