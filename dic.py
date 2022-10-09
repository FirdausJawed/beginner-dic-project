import json
from difflib import get_close_matches
data = json.load(open("data.json"))
# print(data["fog"])

word=input("enter the word you want to search ")

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title]
    elif word.upper() in data:
        return data[word.upper()]   
    elif len(get_close_matches(word,data.keys())) >0:
        print("did you mean %s instead" % get_close_matches(word,data.keys())[0])
        decide=input("press y for yes and n for no\n")

        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide=="n":
            print("check it again")
        else:
            print("entered wrong key")
        
    else:
        print("check it again")

output=translate(word)
# print(output)

if type(output)==list:
    for item in output:
        print(item)

else:
    print(output)        