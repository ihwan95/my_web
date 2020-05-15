#!C:\Users\xzavi\AppData\Local\Programs\Python\Python37-32\python.exe
import os
import cgi
import sys
# import cgitb
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')
# cgitb.enable(display=0, logdir='/tmp/user/cgi-bin')

form = cgi.FieldStorage()

# fileitem = form["filename"]
title = form["title"].value
context = form["context"].value
try:
    # if fileitem.filename:
    #     fn = os.path.basename(fileitem.filename)
    #     open('/tmp/'+ fn, 'wb').write(fileitem.file.read())
    #     message = "The file \'"+fn+"\'was uploaded succesfully"
    # else:
    #     message = 'No file was uploaded'

    search_dir = "List/"
    with open(search_dir + title, 'w', encoding="utf-8") as f:
        f.write(context)

    print(f"""Location: index.py?id={title}\n""")
except Exception as e:
    print(f"""<script>
                alert("Errorcode = {e}")
                location.replace('index.py')
            </script>""")
