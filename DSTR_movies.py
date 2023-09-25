#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

class MovieDataset:
    def __init__(self, data_file):
        self.data_file = data_file
        self.df = self.load_data()

    def load_data(self):
        try:
            # Load data from CSV file into a DataFrame
            return pd.read_csv("archive/movies_metadata.csv")
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return None

    def number_of_unique_movies(self):
        if self.df is not None:
            return self.df['title'].nunique()
        else:
            return 0

    def average_rating(self):
        if self.df is not None:
            return self.df['vote_average'].mean()
        else:
            return 0.0

    def top_rated_movies(self, n=5):
        if self.df is not None:
            return self.df.nlargest(n, 'vote_average')
        else:
            return None

    def movies_released_each_year(self):
        if self.df is not None:
            return self.df['release_date'].str[:4].value_counts().reset_index().rename(columns={'index': 'Year', 'release_date': 'Movie Count'})
        else:
            return None

    def movies_in_each_genre(self):
        if self.df is not None:
            genres = self.df['genres'].str.split('|', expand=True).stack().reset_index(level=1, drop=True)
            return genres.value_counts().reset_index().rename(columns={'index': 'Genre', 0: 'Movie Count'})
        else:
            return None

if __name__ == "__main__":
    dataset = MovieDataset("movies_metadata.csv")

    # Perform operations and print results
    print(f"Number of unique movies: {dataset.number_of_unique_movies()}")
    print(f"Average rating of all movies: {dataset.average_rating()}")
    print("Top 5 highest rated movies:")
    top_rated = dataset.top_rated_movies()
    if top_rated is not None:
        print(top_rated[['title', 'vote_average']])
    else:
        print("No data available.")

    print("Number of movies released each year:")
    movies_by_year = dataset.movies_released_each_year()
    if movies_by_year is not None:
        print(movies_by_year)
    else:
        print("No data available.")

    print("Number of movies in each genre:")
    movies_in_genre = dataset.movies_in_each_genre()
    if movies_in_genre is not None:
        print(movies_in_genre)
    else:
        print("No data available.")



# In[ ]:




