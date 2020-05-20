#!C:\Users\xzavi\AppData\Local\Programs\Python\Python37-32\python.exe
import os
import cgi
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


# 저장 폴더 선택
global search_dir
search_dir = "List/"

# 글 목록 생성
def make_list():
    files = os.listdir(search_dir)
    files.sort(key=lambda x: os.path.getctime(os.path.join(search_dir, x)), reverse = True)
    global nav_list
    nav_list = ""
    for name in files:
        nav_list = nav_list + f'<li><a href="index.py?id={name}"> {name} </a> </li>\n'
    return nav_list

# button 생성
def make_button(pageId):
    if pageId == "Home":
        buttons =f"""<button onclick = "location.href='index.py?id=Post';" class='button' id="post"> 새 글 </button>"""
    elif pageId == "Post":
        buttons = ""
    else:
        buttons = f"""<button onclick = "location.href='index.py?id=Post';" class='button' id="post"> 새 글 </button>
                        <div><button onclick = "location.href='modify.py?id={pageId}';" id='modify'> 수정 </button>
                        <button onclick = "location.href='process_delete.py?id={pageId}'; confirm('정말 삭제하시겠습니까');" id='delete'> 삭제 </button></div>"""
    return buttons

# 본문 생성
def make_context(pageId):
    if pageId == "Home" or pageId== "Post":
        context = open(pageId,'r', encoding='utf-8').read()
    else:
        context = open(search_dir + pageId,'r', encoding='utf-8').read()
    return context
    
# HTML코드 출력
def HTML(nav_list, buttons, title, context):
    print("Content-Type: text/html; charset=utf-8;\n\n")

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
