#!C:\Users\xzavi\AppData\Local\Programs\Python\Python37-32\python.exe
import os
import cgi
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')


from index import HTML


form = cgi.FieldStorage()
title_past = form["title_past"].value
context = form["context"].value

title = "Modify"
context = f"""<form action = "process_modify.py" method = "post">
                    <input type="hidden" name = "title_past" value = "{title_past}">
                    <p> <input type="text" name = "title" placeholder = "{title_past}"> </p>
                    <p> <textarea  name = "context"> {context} </textarea> </p>
                    <input type="submit" onclick="return confirm('수정하시겠습니까?')">
                </form>"""


HTML(title, context)
