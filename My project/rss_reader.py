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
        
rss_reader('https://opt-opt-opt.ru/catalog/letnyaya_obuv/gd2016_l01_3_bezh_bosonozhki_zhenskie_36_41_10')