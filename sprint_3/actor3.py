def read_and_process_file(file_path):
    highest_avg = 0
    highest_avg_actor = None

    with open(file_path, 'r') as file:
        next(file)  # Skip the first line (header)
        for line in file:
            # Divide the line into separate fields
            fields = line.split(',')
            
            # Handle the 'Robert Downey, Jr.' exception
            if "Robert Downey" in fields[0]:
                fields[0] = "Robert Downey Jr."
                fields[1] = fields[2]
                fields.pop(2)
            
            # Extract the fields we are interested in
            actor, total_gross, number_of_movies = fields[0], fields[1], fields[2]

            # Compute the average gross for the actor
            avg_gross = float(total_gross) / float(number_of_movies)
            
            # If this actor's average gross is the highest we've seen, remember them
            if avg_gross > highest_avg:
                highest_avg = avg_gross
                highest_avg_actor = actor
                
    return highest_avg_actor, highest_avg


file_path = r"D:\Documentos\Compass tudo\exemplo_pb\sprint_3\actors.csv"
actor, avg = read_and_process_file(file_path)

print(f'O ator com a maior média de faturamento por filme é {actor} com uma média de {avg}')
 