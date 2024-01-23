from urllib.request import urlopen
from xml.etree.ElementTree import parse

u = urlopen('')
doc = parse(u)
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

print(title)
print(date)
print(link)
print()