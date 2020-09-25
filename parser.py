import json
import markdown

# Special Characters like “, ” & ’ 
chars = {
    '\u201c':'\"',
    '\u201d':'\"',
    '\u2019':'\'',
    '\n':'<br />'
}

class Files():
    __slots__=['mdFile','jsonFile']
    
    def __init__(self,md,js):
        '''
        Calling the two files that will be manipulated
        '''
        jokesFile = open(md, encoding='utf8')
        self.mdFile = markdown.markdown(jokesFile.read())
        jokesFile.close()
        
        self.jsonFile = open(js,'w+')

    def parsing(self):
        '''
        Conversion and closing of the file.
        '''
        jsonJokes = { 'jokes' : []}

        content = self.mdFile.split('<hr />')
        content.pop(0) # Deletes the title section
        mdown = markdown.Markdown()
        for joke in content:
            jokeMarkdown = mdown.convert(joke)
            for key in chars:
                jokeMarkdown= jokeMarkdown.replace(key, chars[key])
            jsonJokes['jokes'].append(jokeMarkdown)
            mdown.reset()
        
        self.jsonFile.write(json.dumps(jsonJokes,ensure_ascii=True))
        self.jsonFile.close()

def main():
    files = Files("README.md","jokes.json")
    files.parsing()

if __name__=="__main__":
    main()