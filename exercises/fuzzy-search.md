### Theoretical - Fuzzy Search

#### **References:**

Search Algorithms:
- https://study.com/academy/lesson/string-searching-algorithms-methods-types.html
- https://www.geeksforgeeks.org/searching-algorithms/

Searching and Sorting Algorithms Book:
- http://www.cs.carleton.edu/faculty/adalal/teaching/f04/117/notes/searchSort.pdf 

Fuzzy Search:
- https://en.wikipedia.org/wiki/Approximate_string_matching

Python Package:
- https://github.com/seatgeek/fuzzywuzzy
- https://github.com/ztane/python-Levenshtein/

Levenshtein Distance:
- https://en.wikipedia.org/wiki/Levenshtein_distance
- https://youtu.be/MiqoA-yF-0M

Levenshtein Distance Tutorials:
- https://stackabuse.com/levenshtein-distance-and-text-similarity-in-python/
- https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
- https://www.elastic.co/blog/found-fuzzy-search


### Practical - Fuzzy Search

```python
def distance(string, pattern):
    string = " " + string.lower() # Make lowercase
    pattern = " " + pattern.lower() # Make lowercase
   
    matrix = {}  Empty matrix

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

print("-------------------\nResults:\n")

# Display first 3 similar movies
for i in range(len(sorted_list)):
    print(sorted_list[i])
    if (i > 3):
        break
```