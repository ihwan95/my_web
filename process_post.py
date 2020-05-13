#!C:\Users\xzavi\AppData\Local\Programs\Python\Python37-32\python.exe
import os
import cgi
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

form = cgi.FieldStorage()
title = form["title"].value
context = form["context"].value

with open("List/" + title, 'w', encoding="utf-8") as f:
  f.write(context)

print("Location: index.py?id=" + title)
print()
