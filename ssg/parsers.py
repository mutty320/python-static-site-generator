import shutil
from typing import List
from pathlib import Path

class Parser:
    extentions: List[str] = []

    def valid_extension(self, extention):
        for exten in self.extentions:
            if exten == extention:
                return True
    def copy(path, source, dest):
        shutil.copy2(path, dest / path.relative_to(source))

    def parse(path: Path, source: Path, dest: Path):

        raise NotImplementedError

    def read(path):
        with open(path, 'r') as f:
            contents = f.read()
    return contents

    def write(path, dest, content, ext = ".html"):
        full_path = self.dest / path.with_suffix(ext).name

        with open(full_path, 'w') as f:
            f.write(content)

class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]
    def parse(path: Path, source: Path, dest: Path):
        super().copy(path, source, dest)
