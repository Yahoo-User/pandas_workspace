from urllib.request import urlopen

res = urlopen('http://pythonscraping.com/pages/page1.html')
html = res.read().decode('utf8')

print(html)
