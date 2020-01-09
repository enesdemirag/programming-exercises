### Theoretical - Fuzzy Search

Searching is a key component of big and complex systems. There are many different ways to find what we are looking for. For instance, if we want to find the location of a file in a directory, we enter the file name and the search algorithm looks ever directory and returns the file when it finds. But sometimes we do not know the exact name of the file. In this case, traditional searchinf algorithms are not sufficient.

For these type of problems, we use Fuzzy Search Algorithms. This way we can find the file, even if input was not completely correct. This algorithm looks for similarity. This method can be used in many cases.

To find the similarity, we need to give ranks to every file and return the one with best rank. In order to do this, we will use _[Levenshtein Distance](https://youtu.be/MiqoA-yF-0M)_ method.

### Practical - Fuzzy Search

Write a function that gets an input, and returns the most similar results in a file.
Example movie list is [here](materials/fuzzy-search/movielist.txt).

```python
def distance(string, pattern): # Levenshtein Distance
    string = " " + string.lower() # Make lowercase
    pattern = " " + pattern.lower() # Make lowercase
   
    matrix = {} # Empty matrix

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
```

Full code can be accessed from [here](materials/fuzzy-search/search.py).

#### **References:**

_Search Algorithms:_
- https://study.com/academy/lesson/string-searching-algorithms-methods-types.html
- https://www.geeksforgeeks.org/searching-algorithms/

_Searching and Sorting Algorithms Book:_
- http://www.cs.carleton.edu/faculty/adalal/teaching/f04/117/notes/searchSort.pdf 

_Fuzzy Search:_
- https://en.wikipedia.org/wiki/Approximate_string_matching

_Python Package:_
- https://github.com/seatgeek/fuzzywuzzy
- https://github.com/ztane/python-Levenshtein/

_Levenshtein Distance:_
- https://en.wikipedia.org/wiki/Levenshtein_distance

_Levenshtein Distance Tutorials:_
- https://stackabuse.com/levenshtein-distance-and-text-similarity-in-python/
- https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
- https://www.elastic.co/blog/found-fuzzy-search