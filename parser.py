from emoji import UNICODE_EMOJI, demojize
import json     # JSON files tools
import os     # Create folders in the computer
from pathlib import Path     # Joins paths from parent to child
import re     # Helps deleting unnecesary linespaces


# Special Characters like “, ” & ’
chars = {
    '\u201c': '\"',
    '\u201d': '\"',
    '\u2019': "\'"
}


class Parser:
    __slots__ = ['mdName', 'mdFile', 'folder', 'js']

    def __init__(self, md, folder, js):
        # Params of interest
        self.mdName = md
        self.folder = folder
        self.js = folder + '/{}.json'.format(js)
        self.mdFile = None

    def __readingMD(self):
        # Reading the md file
        print("Reading the markdown file...")
        jokesFile = open(self.mdName, encoding='utf8')
        self.mdFile = jokesFile.read()
        jokesFile.close()
        print("Done.\n+++++")
        return self.mdFile

    def __setUp(self):
        # Setting up the folder
        print("Checking for folder...")
        try:
            cwdFolder = os.path.abspath(self.folder)
            os.mkdir(cwdFolder)
        except OSError:
            message = "Creation of \"{}\" failed. It already exists.\nContinuing process".format(
                self.folder)
        else:
            message = "Successfully created the directory {} ".format(
                self.folder)
            print(message)

    def extract_emojis(self, s):
        return ''.join(c for c in s if c in UNICODE_EMOJI)

    def __parsing(self):
        # Parses md file into JSON
        md_content = self.__readingMD()
        jsonJokes = {'jokes': []}
        content = re.split('(\*{3})|(\*\s\*\s\*)', md_content)
        content.pop(0)  # Deletes the title section
        for joke in content:
            if joke == None:
                continue
            if re.match('(\*{3})|(\*\s\*\s\*)', joke) == None:
                if joke == '\n'*len(joke):
                    continue
                while joke[0] == '\n':
                    joke = joke[1:]
                while joke[-1] == '\n':
                    joke = joke[:-1]
                for key in chars:
                    joke = joke.replace(key, chars[key])
                if len(self.extract_emojis(joke)):
                    print(
                        "These emojis affect the parsing:\n>>>{}\nin this joke:\n>>>{}\n\nChange it in order to make the parsed joke readable".format(
                            self.extract_emojis(joke), joke))
                    print(''.join([demojize(i)
                                   for i in self.extract_emojis(joke)]))
                jsonJokes['jokes'].append(joke)

        jsonFile = open(self.js, 'w+')
        jsonFile.write(json.dumps(jsonJokes, ensure_ascii=True))
        jsonFile.close()

    def operate(self):
        self.__setUp()
        self.__parsing()


def main():
    parser = Parser("README.md", "parserOutput", "jokes")
    parser.operate()


if __name__ == "__main__":
    main()
