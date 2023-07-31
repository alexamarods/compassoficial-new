import pandas as pd

# Load the data
actors_df = pd.read_csv('D:\\Documentos\\Compass tudo\\exemplo_pb\\sprint_7\\Trabalho_pandas\\actors.csv')

# Identify the actor/actress with the highest average per movie
max_avg_actor = actors_df.loc[actors_df['Average per Movie'].idxmax()]

print("The actor with the highest average per movie is:", max_avg_actor['Actor'])
import pandas as pd

