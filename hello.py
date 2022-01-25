#!/usr/bin/env python3

import os
import json


#Q1 PRINT OUT AL ENV VARIABLES AS PLAIN TEXT
# print("Content-Type: text/plain")  # Specify we want plain text
# print()
# print(os.environ)
##  RUN  http://localhost:8080/hello.py with cgi_server.py run on the background

# Q2 PRint ENV VARIABLES AS JSON
print("Content-Type: application/json") # specify we want json 
print()
print(json.dumps(dict(os.environ), indent=2))  # Better formatting
# RUN  http://localhost:8080/hello.py

# Q2 PRINT QUERY PARAMETER IN HTML
# print("Content-Type: text/html")  # Specify we want html
# print()
# print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")

#RUN http://localhost:8080/hello.py?thisisaquery to get the output


#Q3  report the user’s browser in the HTML.
