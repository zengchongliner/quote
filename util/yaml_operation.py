import yaml

class Yaml_Operation:

    def __init__(self, url):
        with open(url) as yaml_file:
            self.data = yaml.load(yaml_file, yaml.FullLoader)

    def get_locator(self, page, local):
        return self.data[page][local]