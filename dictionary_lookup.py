import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def definition(w):
       w = w.lower()
       match = get_close_matches(w,data.keys(),cutoff = 0.8)

       if w in data:
           return data[w]
       elif len(match) > 0:
           yn =  input("Did you mean %s instead? Enter Y if yes, N if no:  " % match[0])
           if str.islower(yn): yn = str.swapcase(yn)

           if yn == "Y":
                return data[match[0]]
           elif yn == "N":
                return "The word doesnt exit. Please enter another word"
           else:
                return "We do not understand"
       else:
           return "The word doesnt exit. Please enter another word"
          
word = input("Enter word: ")

output = definition(word)

if type(output) == list:
    for item in output:
          print(item)
else:
    print(output)