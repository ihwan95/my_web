#!C:\Users\xzavi\AppData\Local\Programs\Python\Python37-32\python.exe
import os
import cgi
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


try:
    print("Content-Type: text/html; charset=utf-8\n\n")


    # 목차 생성
    search_dir = "List/"
    files = os.listdir(search_dir)
    files = [os.path.join(search_dir, f) for f in files]
    files.sort(key=lambda x: os.path.getmtime(x), reverse = True)
    nav_list = ""
    for name in files:
      name=name[5:]     # root폴더("List/") 없애기
      nav_list = nav_list + f'<li><a href="index.py?id={name}"> {name} </a> </li>\n'

     # id값 확인
    form = cgi.FieldStorage()
    change = ""   # delete 버튼
    if 'id' in form:
        pageId = form["id"].value
        # 게시물 열람할 때
        if pageId != "Post":
            description = open('List/' + pageId,'r', encoding='utf-8').read()
            change = f"""<a href='Delete.py?id={pageId}' class='button' id='delete' onclick="return confirm('정말 삭제하시겠습니까?')"> Delete </a>"""
        # Post할 때
        else:
            description = open(pageId,'r', encoding='utf-8').read()
    # id값이 없을 때
    else:
        pageId = "Home"
        description = open(pageId,'r', encoding='utf-8').read()
except:
    print("""
    <script>
        alert("글이 존재하지 않습니다.")
        location.replace('index.py')
    </script>""")

# HTML 코드 시작
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
          <a href= 'index.py?id=Post' class='button' id="post"> Post </a>
          {change}
        </div>
        <div class=article>
          <div id="title"> {pageId} </div>
          <div id="context"> {description} </div>
        </div>
      </main>
      <a href="https://github.com/ihwan95/my_web" target="_blank" onclick="alert('github페이지로 이동합니다.')" id="github"> GITHUB link </a>
    </section>
  </body>

</html>
""")
