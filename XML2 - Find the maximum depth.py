# Enter your code here. Read input from STDIN. Print output to STDOUT
# Author : Vineet

import xml.etree.ElementTree as etree

def depth (root):
    return max([0] + [depth(child) + 1 for child in root])

N = int(raw_input())
xml = ""
for i in range(N):
    xml += str(raw_input())

tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()

print depth(root)
