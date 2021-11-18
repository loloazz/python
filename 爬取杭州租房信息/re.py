import re

key="<html><h1>hello world<h1></html>"
print(re.findall('<h1>(.*)<h1>',key)[0])