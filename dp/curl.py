#!/bin/python
import os

url = "http://192.168.1.18:8000/api/"
a = ["release/all", "release/2.3.0", "tcinfo/2.3.0", "tcstatus/2.3.0"]
#a = ["tcinfo/master", "tcstatus/master"]

for i in a:
	print(i)
	os.system("curl " + url + i)
