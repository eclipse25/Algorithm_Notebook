#!/usr/bin/env python

import os
from urllib import parse

HEADER = """
## ✨알고리즘 문제 풀이 목록✨

[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=eclipse34)](https://solved.ac/eclipse34/)
"""

def main():
    content = ""
    content += HEADER

    directories = []
    solveds = []

    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        category = os.path.basename(root)

        if category == 'images':
            continue

        directory = os.path.basename(os.path.dirname(root))

        if directory == '.':
            continue

        if directory not in directories:
            if directory in ["백준", "프로그래머스"]:
                content += "<h3 style='font-weight: bold;'>📚 {}</h3>\n".format(directory)
            else:
                content += "<h3 style='font-weight: bold;'>🚀 {}</h3>\n".format(directory)
                content += "<div style='width: 800px;'>\n"
                content += "<table>\n"
                content += "<thead>\n"
                content += "<tr><th style='width: 650px;'>문제번호</th><th style='width: 150px;'>링크</th></tr>\n"
                content += "</thead>\n"
                content += "<tbody>\n"
            directories.append(directory)

        for file in files:
            if category not in solveds:
                file_path = os.path.join(root, file)
                link = parse.quote(file_path)
                html_link = '<a href="{}">링크</a>'.format(link)
                content += "<tr><td>{}</td><td>{}</td></tr>\n".format(category, html_link)
                solveds.append(category)
                print("category : " + category)
        
        if directory in directories:
            content += "</tbody>\n</table>\n</div>\n"

    with open("README.md", "w") as fd:
        fd.write(content)

if __name__ == "__main__":
    main()
