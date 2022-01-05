import json

jokes = {}
with open("../readme.md", "r", encoding="utf8") as file:
    text = file.read()
    text = text.replace(
        "***", "* * *"
    )  # Because some jokes aren't delimited by spaced-out asterisks
    separatedjokes = text.split("* * *")

    for idx, joke in enumerate(separatedjokes[1:], 1):
        # skipping the first joke because that's just repo header
        jokes["joke#" + str(idx)] = joke.strip().strip("#")
        # remove redundant \n, \t and whitespaces at beginning & end of joke
        # '#' split because certain jokes have a ####Ques ####Answer format

with open("Jokes.json", "w") as outfile:
    json.dump(jokes, outfile)
