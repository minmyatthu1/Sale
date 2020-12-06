import json

data = json.load(open("data.json"))


def translate(w):

    while True:
        if w in data:
            return data[w]

        else:
            return "Sorry. The word you entered doesn't exist in current dictionary. enter '.' to exit "


while True:
    word = input("Enter a word: ")
    word = word.lower
    print(translate(word))

    if word == ".":
        break
