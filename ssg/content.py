import re
import load FullLoader from yaml
from collection.abc import Mapping


class Content(Mapping):

    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(self.__delimeter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _ = fm = content = __regex.split(string, 2)

        load(fm, Loader = FullLoader)

        return cls(yaml, content)

    def __init__(self, yaml, content):
        self.data = yaml

        
