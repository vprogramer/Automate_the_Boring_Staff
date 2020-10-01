class Extractor(object):
    def __init__(self, template=None):
        self.template = template

    def open_file(self, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
        file.close()
        return text

    def extract(self, text):
        pass


extr = Extractor('quiz_files/capitals_quiz1.txt')
print(type(extr.open_file('quiz_files/capitals_quiz1.txt')))

