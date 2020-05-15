#!C:\Users\xzavi\AppData\Local\Programs\Python\Python37-32\python.exe
import os
import cgi
import sys
import _function
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

## id값  확인
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
else:
    pageId = "Home"

## 실행문
try:
    if __name__ == "__main__" :
        nav_list = _function.make_list()
        buttons = _function.make_button(pageId)
        context = _function.make_context(pageId)
        _function.HTML(nav_list,buttons,pageId,context)
except Exception as e:
    print(f"""<script>
                alert("페이지가 존재하지 않습니다. errorcode = {e}")
                location.replace('index.py')
            </script>""")
