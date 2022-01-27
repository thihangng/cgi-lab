
#!/usr/bin/env python3
# import cgi
# import cgitb
# cgitb.enable()

# from templates import login_page, secret_page, after_login_incorrect
# import secret
# import os
# from http.cookies import SimpleCookie


# # # CREATE LOGIN FORM

# s = cgi.FieldStorage()
# username = s.getfirst("username")
# password = s.getfirst("password")

# # Print to html
# print("Content-type: text/html")
# print()

# #load login page, print user form info
# if not username and not password:
#     print(login_page())
# elif username == secret.username and password == secret.password:
#     print(secret_page(username, password))
# else:
#     print(after_login_incorrect())    



# # RUN  http://localhost:8080/login.py to see the result




# LOGIN WITH COOKIE

import cgi
import cgitb
from errno import ENETRESET
from webbrowser import BaseBrowser
from xml.sax.handler import EntityResolver
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http.cookies import SimpleCookie


# CREATE LOGIN FORM

s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

# Check if correct login 
form_o = username == secret.username and password == secret.password

# SET UP COOKIE, simple cookie object from http cookie
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get("username"):  #check if cookie already exists
    # Extract username from cookie in the browser
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value


# Check cookie user/pass = secret user/pass
cookie_ok = cookie_username == secret.username and cookie_password == secret.password

# SET user/pass to cookie user/pass
if cookie_ok:
    username = cookie_username
    password = cookie_password

print("Content-Type: text/html")
if form_o:
    print(f"set-cookie: username={username}")
    print(f"set-cookie: password={password}")
print()

# LOAD HTML PAGES
if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())
    
# THIS WAY IF WE LOGIN, WHEN REFRESH, WE STAY LOGIN
# RUN  http://localhost:8080/login.py to see the result

# Q7: fake cookie
# go to console in your BaseBrowser
# javascript:document.cookie="{username} = {secret.username}"
# DO THE SAME THING FOR PASSWORD