#!C:\Users\xzavi\AppData\Local\Programs\Python\Python37-32\python.exe
import os
import cgi
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

# search_dir = "List/"

# Get filename here.
form = cgi.FieldStorage()
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('/tmp/' + fn, 'wb').write(fileitem.file.read())

   message = 'The file "' + fn + '" was uploaded successfully'

else:
   message = 'No file was uploaded'

print( f"""
Content-Type: text/html\n\n
<html>
<body>
   <p>{message}</p>
</body>
</html>
""")
