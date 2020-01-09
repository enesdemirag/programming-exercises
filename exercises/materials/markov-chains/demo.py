import random

text = open("file.txt").read().split() # Read Source Text
wordsDict = dict()

def addWords(text): # Add every different word to the dictionary
    global wordsDict
    for word in text:
        if not word in wordsDict:
            wordsDict[word] = list()
        if text.index(word) == (len(text) - 1):
            break

def addToPossibilities(word, nextWord): # Add next words to each list
	wordsDict[word].append(nextWord)

def findIndex(word, indexNum): # Find the index of word in source text
	indexes =  [i for i, e in enumerate(text) if e == word] # Indexes of all occurence
	return indexes[indexNum]

def learn(text):
	addWords(text)
	for word in text:
		if text.index(word) == (len(text) - 1): # Don't check last word
			break
		indexNum = len(wordsDict[word]) # Next words of previous occurrence
		addToPossibilities(word, text[findIndex(word, indexNum) + 1])

def run(n, initialWordIndex):
    currentWord = text[initialWordIndex] # First word
    for i in range(n): # print next n words
        print(currentWord, end = " ")
        nextWord = random.choice(wordsDict[currentWord]) # Select random word next word from list
        currentWord = nextWord

# Generate text with 100 words
learn(text)
run(100, 0)