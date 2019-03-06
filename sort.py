#! C:\Program Files\Python37\python
def sort1(string1):
    k=[]
    #string1="hello world"
    for i in string1.split():
        k.append(i)
    k=sorted(k)
    k=' '.join(k)
    print(k)
import cgi
print("content-type:text/html\n")
print("<html>")
print("<head><title>calculator</title>")
print("</head>")
print("<body>")
form=cgi.FieldStorage()
string1=form.getvalue("string1")
print('<form method="post" action="sort.py">')
print('<p>Enter the string<input type="text" name="string1"/></p>')
print('<input type="submit" value="submit"/>')
print('<br>')
print('<br>')
print("</body>")
print("</html>")
print("\n")
sort1(string1)
    
