from itertools import count
from jinja2 import Environment, FileSystemLoader

INDEX = "index.html"
TITLE = "The Weird Dungeon Core, by Vorquel"

def get_chapters():
    chaps = [{"link":INDEX}]
    try:
        for index in count(1):
            with open(f"chapters/{index}.txt") as file:
                file = file.read()
            chaps[-1]["next"] = f"chapter-{index}.html"
            chaps.append({
                "title": TITLE,
                "home": INDEX,
                "prev": chaps[-1]["link"],
                "link": chaps[-1]["next"],
                "next": INDEX,
                "text": [("<hr>" if split == "---" else {
                    "lines": (lines := split.split("\n"))[(split[0] == "."):],
                    "class": (lines[0][1:] if split[0] == "." else "txt"),
                }) for split in file.split("\n\n")],
            })
    except OSError:
        pass
    return chaps[1:]

def main():
    env = Environment(
        keep_trailing_newline=True,
        loader=FileSystemLoader("jinja/"),
    )
    home_tmpl = env.get_template(INDEX)
    chap_tmpl = env.get_template("chapter.html")
    chaps = get_chapters()
    with open("site/index.html", "w") as file:
        file.write(home_tmpl.render(
            chaps=[chap["link"] for chap in chaps],
            title=TITLE,
        ))
    for chap in chaps:
        with open(f"site/{chap['link']}", "w") as file:
            file.write(chap_tmpl.render(chap))

if __name__ == "__main__":
    main()
