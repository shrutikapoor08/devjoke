import json     # JSON files tools
import os     # Create folders in the computer
from pathlib import Path     # Joins paths from parent to child
import re     # Helps deleting unnecesary linespaces

# Special Characters like “, ” & ’ 
chars = {
    '\u201c':'\"',
    '\u201d':'\"',
    '\u2019':"\'"
}

# Params of interest
md = "README.md"
folder = "parserOutput"
js = folder+"/jokes.json"

# Reading the md file
def readingMD():
    jokesFile = open(md, encoding='utf8')
    mdFile=jokesFile.read()
    jokesFile.close()
    return mdFile

# Setting up the folder
def setUp():
    try:
        cwdFolder = os.path.abspath(folder)
        os.mkdir(cwdFolder)
    except OSError:
        message="Creation of \"{}\" failed. It already exists".format(folder)
    else:
        message="Successfully created the directory {} ".format(folder)
    print(message)

# Parses md file into JSON
def parsing():
    md_content = readingMD()
    jsonJokes = { 'jokes' : []}

    content = re.split('(\*{3})|(\*\s\*\s\*)',md_content)
    content.pop(0) # Deletes the title section
    for joke in content:
        if joke==None:
            continue
        if re.match('(\*{3})|(\*\s\*\s\*)',joke)==None:
            if joke=='\n'*len(joke): continue
            while joke[0]=='\n': joke=joke[1:]
            while joke[-1]=='\n': joke=joke[:-1]
            for key in chars:
                joke= joke.replace(key, chars[key])
            jsonJokes['jokes'].append(joke)
    
    jsonFile = open(js,'w+')
    jsonFile.write(json.dumps( jsonJokes, ensure_ascii=True ))
    jsonFile.close()

def main():
    setUp()
    parsing()


if __name__=="__main__":
    main()