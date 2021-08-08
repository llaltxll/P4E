txt = 'but soft what light in yonder window breaks'
words = txt.split()

# DSU Abbreviation of “decorate-sort-undecorate”, a pattern that involves building
# a list of tuples, sorting, and extracting part of the result

# Build a list of touples (length of word, word)
t = list()
for word in words:
  t.append((len(word), word))
# Sort the list using the first element (length of word), use second element (word) to brake ties 
t.sort(reverse=True)

# put the newley ordered words in t into a new list res ommiting the length
res = list()
for length, word in t:
  res.append(word)
  
print(res)