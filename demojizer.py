from emoji import UNICODE_EMOJI, demojize
import sys


class Demojizer:
    __slots__ = ['mdFile', 'mdName']

    def __init__(self, mdFile):
        try:
            t = open(mdFile, 'r', encoding='utf8')
            self.mdFile = t.read()
            t.close()
            self.mdName = mdFile
        except FileNotFoundError:
            message = "The name of the file doesn't exist :(.".format(
                self.mdFile)
            print(message)
            sys.exit()

    def __demojize(self):
        self.mdFile = demojize(self.mdFile)

    def refactor(self):
        self.__demojize()
        try:
            final = open(self.mdName[:-3] + '_demojized.md', 'x')
            print('File {}_demojized.md was created. Writing...'.format(
                self.mdName[:-3]))
            final.write(self.mdFile)
            final.close()
        except FileExistsError:
            print('File {}_demojized.md is being overwritten...'.format(
                self.mdName[:-3]))
            final = open(self.mdName[:-3] + '_demojized.md', 'w')
            final.write(self.mdFile)
            final.close()


def main():
    # Change this string to call the file you want to demojize
    d = Demojizer("CONTRIBUTING.md")
    d.refactor()


if __name__ == "__main__":
    main()
