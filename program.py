""""Write a function that takes a key value and returns the output for that key.
Incorporate the loading of a json file"""
import json
from difflib import get_close_matches
from difflib import SequenceMatcher

# Complete task of returning simple definition
data = json.load(open('data.json'))
user_input = input("Please enter a word  to define: ")


# Implementation of Sequence Matcher
def get_ratio():
    """Return the ratio match of user input and words in dictionary """
    for w in data:
        print(SequenceMatcher(None, user_input, w).ratio())


def translate(word):
    """Used to return definitions"""
    word = word.lower()
    if word in data:  # dealing with non-existing words in data
        return data[word]
    # Implementationof my solution to resolve definition problems for Delhi
    # and Paris
    elif word == "paris":
        word = "Paris"
        return data[word]
    elif word == "delhi":
        word = "Delhi"
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead. Enter Y if yes, N if No: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word  doesn't exist, Please double check it"
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist. Please double check typed word"


output = translate(user_input)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
