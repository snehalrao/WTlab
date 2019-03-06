#! C:\Program Files\Python37\python
def cal(a,b,op):
    if op=="addition":
        print(int(a)+int(b))
    elif op=="subtraction":
        print(int(a)-int(b))
    elif op=="multiplication":
        print(int(a)*int(b))
    elif op=="modulus":
        print(int(a)%int(b))
#def __main__(): 
 #   print("enter the numbers")
 #   a=int(input())
  #  b=int(input())
 #   print("enter the required operation")
  #  op=input()
  #  k=cal(op,a,b)
 #   print(k)
import cgi
print("content-type:text/html\n")
print("<html>")
print("<head><title>calculator</title>")
print("</head>")
print("<body>")
form=cgi.FieldStorage()
a=form.getvalue("first")
b=form.getvalue("second")
op=form.getvalue("operation")
print('<form method="post" action="arthimatic.py">')
print('<p>Enter the first number<input type="text" name="first"/></p>')
print('<p>Enter the second number<input type="text" name="second"/></p>')
print('<p>enter the opeartion:</p><select name="operation"> <option>addition</option><option>subtraction</option><option>multiplication</option><option>modulus</option>></select>')
print('<input type="submit" value="submit"/>')
print('<br>')
print('<br>')
print("</body>")
print("</html>")
print("\n")
cal(a,b,op)
