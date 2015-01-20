# Enter your code here. Read input from STDIN. Print output to STDOUT
# Author : Vineet

import re
pattern = '^(?=[MDCLXVI])M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
roman = str(raw_input())
if re.search(pattern, roman):
    print 'True'
else:
    print 'False'