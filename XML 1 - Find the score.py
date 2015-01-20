# Enter your code here. Read input from STDIN. Print output to STDOUT
# Author : Vineet

import xml.etree.ElementTree as etree

N = int(raw_input())
xml = ""
for i in range(N):
    xml += str(raw_input())

tree = etree.ElementTree(etree.fromstring(xml))
#root = tree.getroot()
count = 0
#count = len(root.attrib)
for element in tree.iter():
    count += len(element.attrib)
print count