from xml.etree.ElementTree import parse, Element
doc = parse(r"My project\work in file\pred.xml")
root = doc.getroot()
root.remove(root.find('sri'))
root.remove(root.find('cr'))
e = Element('spam')
root.insert(2, e)
doc.write('newpred.xml', xml_declaration = True)