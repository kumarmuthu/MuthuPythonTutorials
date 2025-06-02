# 1. Python - URL Processing
# 1.1 Improve your skills in web scraping, fetching data, and managing URLs with Python using urllib
import os
from urllib.parse import urlparse

url = "https://example.com/employees/name/?salary>=25000"
parsed_url = urlparse(url)
print(type(parsed_url))
print("Scheme:", parsed_url.scheme)
print("netloc:", parsed_url.netloc)
print("path:", parsed_url.path)
print("params:", parsed_url.params)
print("Query string:", parsed_url.query)
print("Frgment:", parsed_url.fragment)

# 1.2 Dict info
from urllib.parse import urlparse, parse_qs

url = "https://example.com/employees?name=Anand&salary=25000"
parsed_url = urlparse(url)
dct = parse_qs(parsed_url.query)
print("Query parameters:", dct)

# 1.3 Download image
from urllib.request import urlopen

obj = urlopen("https://www.tutorialspoint.com/images/logo.png")
data = obj.read()
get_cwd = os.getcwd()
img = open(rf"{get_cwd}\Log\img.jpg", "wb")
img.write(data)
img.close()

# 2. Request Object
"""
urllib.request.Request(url, data, headers, origin_req_host, method=None)
"""
from urllib.request import Request, urlopen

obj = Request("https://www.tutorialspoint.com/")
print(f"Request obj: {obj}")
resp = urlopen(obj)
data = resp.read()
print(f"Request Data: {data}")
