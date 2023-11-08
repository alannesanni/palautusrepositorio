from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        dir=toml.loads(content)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(dir["tool"]["poetry"]["name"], dir["tool"]["poetry"]["description"], dir["tool"]["poetry"]["dependencies"], dir["tool"]["poetry"]["group"]["dev"]["dependencies"], dir["tool"]["poetry"]["authors"], dir["tool"]["poetry"]["license"])
