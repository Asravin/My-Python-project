def rss_reader(url):
    from urllib.request import urlopen
    from xml.etree.cElementTree import parse
    
# Загружаем RSS-ленту и парсим ее
    u = urlopen(url)
    doc = parse(u)
    
# Извлекаем и выводим интересующие теги
    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        date = item.findtext('pubDate')
        link = item.findtext('link')
        
        print(title)
        print(date)
        print(link)
        print()
        
rss_reader()