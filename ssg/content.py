import re

from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping):

    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _ = fm = content = cls.__regex.split(string, 2)

        load(fm, Loader = FullLoader)

        return cls(yaml, content)

    def __init__(self, yaml, content):
        self.data = yaml
