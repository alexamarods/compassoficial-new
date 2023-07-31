import pandas as pd

# Load the data
actors_df = pd.read_csv('D:\\Documentos\\Compass tudo\\exemplo_pb\\sprint_7\\Trabalho_pandas\\actors.csv')

# Identify the most frequent movie(s) and their respective frequency
most_frequent_movies = actors_df['#1 Movie'].value_counts()

print("The most frequent movies and their frequencies are:")
print(most_frequent_movies)
