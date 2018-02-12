import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input("did you mean %s instead? enter y if yes or n if no"%get_close_matches(word,data.keys())[0])
        if yn=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="n":
            return "the word does not exist please double check it "
        else:
            return "we did not understand your entry"
    else:
        return "the word does not exist "

word=input("enter the word for which you are searching ")
output=translate(word)

if type(output) == list:
    for items in output:
        print(items)
else:
    print(output)
