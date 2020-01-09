def distance(string, pattern): # Levenshtein Distance
    string = " " + string.lower() # Make lowercase
    pattern = " " + pattern.lower() # Make lowercase
   
    matrix = {}  # Empty matrix

    for i in range(len(string)):
        matrix[i, 0] = i # Fill first row from 0 to length of the string

    for j in range(len(pattern)):
        matrix[0, j] = j # Fill first column from 0 to length of the string
   
    for j in range(1, len(pattern)):
        for i in range(1, len(string)):
            if (string[i] == pattern[j]): # If characters are same
                matrix[i, j] = matrix[i - 1, j - 1] # Write top-left value
            else:
                matrix[i, j] = min(matrix[i - 1, j], matrix[i, j - 1], matrix[i - 1, j - 1]) + 1 # Write 1 + smallest value on top, left, or top-left. 
    
    return matrix[len(string) - 1, len(pattern) - 1] # return the value in last element


movies = open("movielist.txt").read().split("\n") # Get the movie list
movies_with_ranks = {} # Create empty dictionary

query = str(input("Enter movie : ")) # input

for movie in movies: # For every movie in the list
		movies_with_ranks[movie] = distance(movie, query) # Calculate its distance and add to the dictionary 

sorted_list = sorted(movies_with_ranks.keys(), key = lambda i: movies_with_ranks[i]) # Get a list from dictionary sorted based on values

print("Results:")

# Display first 3 similar movies
for i in range(len(sorted_list)):
    print(sorted_list[i])
    if (i > 3):
        break