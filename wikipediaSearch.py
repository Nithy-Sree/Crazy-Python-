# pip install wikipedia

import wikipedia
# query = 'Python'
query = input("Enter the text you want to find: ").strip()

# change the number of sentence to get a larger words summary
results = wikipedia.summary(query, sentences=2)

print(results)
