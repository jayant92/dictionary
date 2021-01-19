import json
from difflib import get_close_matches
data = json.load(open("data.json")) #a file that contains all words and its meanings. this program needs this json file in order to work.

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        yn = input("Did you mean {} instead? Enter Y if yes, or N for no: ".format(get_close_matches(word,data.keys())[0]))
        if yn.lower()=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn.lower()=="n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your input."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for meanings in output:
        print("\n "+ meanings)
else:
    print(output)

