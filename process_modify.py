#!C:\Users\xzavi\AppData\Local\Programs\Python\Python37-32\python.exe
import os
import cgi
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

form = cgi.FieldStorage()
title_past = form["title_past"].value
context = form["context"].value
if "title" in form:
    title = form["title"].value
else: title = title_past

search_dir = "List/"
os.rename(search_dir + title_past, search_dir + title)
with open("List/" + title, 'w', encoding="utf-8") as f:
  f.write(context)

print("Location: index.py?id=" + title)
print()
