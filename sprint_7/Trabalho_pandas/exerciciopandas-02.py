import pandas as pd

# Load the data
actors_df = pd.read_csv('D:\\Documentos\\Compass tudo\\exemplo_pb\\sprint_7\\Trabalho_pandas\\actors.csv')

# Calculate the mean of the 'Number of Movies' column
mean_number_of_movies = actors_df['Number of Movies'].mean()

print("The average number of movies is:", mean_number_of_movies)
import pandas as pd

