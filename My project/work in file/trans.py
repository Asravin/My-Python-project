from xml.etree.ElementTree import Element
def dict_to_xml(tag, d):
    '''
    Преобразуем простой словарь из пар ключей/значений в XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem