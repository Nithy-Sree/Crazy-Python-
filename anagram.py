"""
An Anagram is a word or phrase formed by rearranging the letters of another word or phrase,
usually using the original letters exactly once.
"""

from collections import Counter

def anagram(firstString, secondString):
  return Counter(firstString) == Counter(secondString)

string1 = input().strip()
string2 = input().strip()

print(anagram(string1, string2))
