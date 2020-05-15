#!C:\Users\xzavi\AppData\Local\Programs\Python\Python37-32\python.exe
import os
import cgi
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

# 목차 생성
search_dir = "List/"
files = os.listdir(search_dir)
files.sort(key=lambda x: os.path.getctime(os.path.join(search_dir, x)), reverse = True)
global nav_list
nav_list = ""
for name in files:
    nav_list = nav_list + f'<li><a href="index.py?id={name}"> {name} </a> </li>\n'

# id값 확인
form = cgi.FieldStorage()
global buttons
buttons = ""   # Modify,Delete 버튼
if 'id' in form:
    pageId = form["id"].value
    if pageId == "Post":
        description = open(pageId,'r', encoding='utf-8').read()
    else:
        description = open('List/' + pageId,'r', encoding='utf-8').read()
        description += f"""<form name=modify  action="modify.py" method="hidden">
                                <input type="hidden" name = "title_past" value = "{pageId}">
                                <input type="hidden" name = "context" value = "{description}">
                            </form>"""
        buttons = f"""<button onclick = "location.href='index.py?id=Post';" class='button' id="post"> Post </button>
                    <button onclick = "document.modify.submit();" id='modify'> Modify </button>
                    <button onclick = "location.href='process_delete.py?id={pageId}'; return confirm('정말 삭제하시겠습니까?');" id='delete'> Delete </button>"""
# id값이 없을 때
else:
    pageId = "Home"
    description = open(pageId,'r', encoding='utf-8').read()
    buttons += """<button onclick = "location.href='index.py?id=Post';" class='button' id="post"> Post </button>"""


# HTML 코드 시작
def HTML(title, context):
    print("Content-Type: text/html; charset=utf-8\n\n")

    print(f"""
    <!DOCTYPE html>
    <html>

      <head>
        <meta charset="utf-8">
        <!-- <meta name="viewport" content-"width=device-width, initial-scale-1.0"> -->
        <title> by Ihwan Shin </title>
        <link rel="stylesheet" href="setting/style.css">
        <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="setting/index.js"></script> -->
      </head>

      <body>
        <header>
          <span>
            <a href="index.py"> Draft Page </a>
          </span>
          <!-- <input id="Night_Mode" class=button type="button" value="Night_Mode" onclick="
          day_night();
          "> -->
        </header>
        <section>
          <nav>
            <ol>
              {nav_list}
            </ol>
          </nav>
          <main>
            <div class="function">
              {buttons}
            </div>
            <div class=article>
              <div id="title"> {title} </div>
              <div id="context"> {context} </div>
            </div>
          </main>
          <a href="https://github.com/ihwan95/my_web" target="_blank" onclick="alert('github페이지로 이동합니다.')" id="github"> Web Page_Source </a>
        </section>
      </body>

    </html>
    """)

if __name__ == "__main__" :
    HTML(pageId, description)
# try:
# except:
#     print("""<script>
#                 alert("글이 존재하지 않습니다.")
#                 location.replace('index.py')
#             </script>""")
