#!/usr/bin/python3

print("Content-Type: text/html\n")

import cgi
form = cgi.FieldStorage()
pageId = form["id"].value


print('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>html Document</title>
    <script src="color.js"></script>
  </head>
  <body>
    <h1><a href="index.py">HOME</a></h1>
    <ol>
    <li><a href="index.py?id=html"><h1>HTML</h1></a></li>
    <li><a href="index.py?id=css"><h1>CSS</h1></a></li>
    <li><a href="index.py?id=javascript"><h1>JavaScript</h1></a></li>
    </ol>
    <h2>{title}</h2>
    <p>blablablablablbbla</p>
  </body>
</html>'''.format(title=pageId))
