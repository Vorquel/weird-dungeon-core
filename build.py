from dataclasses import KW_ONLY, dataclass, field
from jinja2 import Environment, FileSystemLoader

@dataclass
class Block:
    _ = KW_ONLY
    cls = "txt"
    lines = field(default_factory=list)

def main():
    env = Environment(keep_trailing_newline=True, loader=FileSystemLoader("jinja/"))
    index = env.get_template("index.html")
    chapter = env.get_template("chapter.html")

if name == "__name__":
    main()
