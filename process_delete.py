#!C:\Users\xzavi\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi
import os
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

form = cgi.FieldStorage()
title = form["id"].value

search_dir = "List/"
os.remove(search_dir + title)

print("Location: index.py")
print()
