from dataclasses import KW_ONLY, dataclass, field
from itertools import count
from os.path import isfile
from jinja2 import Environment, FileSystemLoader

TITLE = "The Weird Dungeon Core, by Vorquel"

@dataclass
class Block:
    _ = KW_ONLY
    cls: str = "txt"
    lines: list[str] = field(default_factory=list)

def from_parts(parts):
    out = []
    for part in parts:
        if part == "---":
            out.append("<hr>")
            continue
        block = Block()
        lines = part.split('\n')
        if lines[0][0] == ".":
            (cls, *lines) = lines
            block.cls = cls[1:]
        block.lines = lines
        out.append(block)
    return out

def main():
    env = Environment(
        keep_trailing_newline=True,
        loader=FileSystemLoader("jinja/"),
    )
    home = env.get_template("index.html")
    chap = env.get_template("chapter.html")
    chapters = {}
    for index in count(1):
        filename = f"chapters/{index}.txt"
        if not isfile(filename):
            break
        with open(filename) as file:
            parts = file.read().split("\n\n")
        chapters[f"chapter-1.html"] = from_parts(parts)
    with open("site/index.html", "w") as file:
        file.write(home.render(
            chapters=[*chapters],
            title=TITLE,
        ))
    for key, parts in chapters.items():
        with open(f"site/{key}", "w") as file:
            file.write(chap.render(
                chapters=[*chapters],
                title=TITLE,
                parts=parts,
                prev="index.html",
                next="index.html",
            ))

if __name__ == "__main__":
    main()
