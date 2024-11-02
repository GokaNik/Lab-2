import xml.dom.minidom as minidom

xml_file = open('currency.xml')
xml_data = xml_file.read()
dom = minidom.parseString(xml_data)
dom.normalize()
elements=dom.getElementsByTagName('Valute')
name=[]
value=[]
for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName=='Name':
                name.append(child.firstChild.data)
        if child.nodeType == 1:
            if child.tagName == 'Value':
                value.append(float(child.firstChild.data.replace(',','.')))
print(name)
print(value)
