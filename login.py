import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http.cookies import SimpleCookie


# CREATE LOGIN FORM

s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

# Print to html
print("Content-type: text/html")
print()

#load login page, print user form info
if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())    

# RUN  http://localhost:8080/login.py to see the result

