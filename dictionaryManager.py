import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def search(word):
    lower_word = word.lower()
    capitalize_word = word.capitalize()
    upper_word = word.upper()
    if lower_word in data:
        return data[lower_word]
    elif capitalize_word in data:
        return data[capitalize_word]
    elif upper_word in data:
        return data[upper_word]
    elif len(get_close_matches(lower_word, data.keys())) > 0:
        if get_close_matches(lower_word, data.keys())[0].lower() == lower_word:
            return data[lower_word]
        return ["The word entered seems incorrect.\n\n Similar word: '%s' " % get_close_matches(lower_word, data.keys())[0]]
    else:
        return ["The word doesn't exist. Please verify it again!"]

