import argparse
import datetime
import pathlib
import re
import sys
import textwrap

from ruamel.yaml import YAML

#import markdown2
import textile


def make_foldername(dt, title, dir, dt_format="%Y-%m-%d"):

    prefix = dt.strftime(dt_format)

    title = title.lower()
    title = re.sub(r"\s+", " ", title)
    title = title.replace(" ", "-")
    title = "".join(list(filter(lambda c: c.isalnum() or c in ["-", "."], title)))
    title = re.sub(r"-+", "-", title)
    title = re.sub(r"\.-", "-", title)
    title = re.sub(r"[\.-]+$", "", title)

    foldername = "{}/{}-{}".format(dir, prefix, title)

    return foldername

def render_hugo_post(dt, content):

    templ = """
    ---
    title: |
      {date} - {title}
    author: "{author}"
    date: "{date}"
    ---

    # {title}
    
    {post}
    """

    templ = textwrap.dedent(templ).lstrip()

    title = content.get("title", "")
    author = content.get("author", "The Fluxbox Team")
    post = content.get("content", "")

    rendered = templ.format(title=title, post=post, author=author, date=dt)

    return rendered

def main():

    parser = argparse.ArgumentParser(
                    prog = "news2hugo",
                    description = "transforms fluxbox-news.yaml to gohugo posts")
    parser.add_argument("-o", "--out-dir", default="news", dest="outFolder")
    args = parser.parse_args()


    news = YAML(pure=True).load(sys.stdin)
    #news = sorted(news.iteritems(), reverse=True)

    for ts in news:
        entry = news[ts]
        dt = datetime.datetime.fromtimestamp(ts)
        foldername = make_foldername(dt, entry["title"], args.outFolder)
        rendered_post = render_hugo_post(dt, entry)
        
        print(ts, dt, foldername)

        folder = pathlib.Path(foldername)
        folder.mkdir(exist_ok=True, parents=True)
        filename = pathlib.PurePath(foldername, "index.md").as_posix()

        with open(filename, "w+") as f:
            f.write(rendered_post)
            f.write("\n")

if __name__ == "__main__":
    main()