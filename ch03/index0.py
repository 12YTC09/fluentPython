"""Build an index mapping word -> list of occurrences"""

import sys
import re

WORD_RE = re.compile('\w+')

index = {}

with open(sys.argv[1],encoding = 'utf-8') as fp:
    for line_no,line in enumerate(fp,1):
        for match in WORD_RE.finditer(line):
            #print(match))
             word = match.group()
             column_no = match.start()+1
             location = (line_no,column_no)
             occurrenceces = index.get(word,[])
             occurrenceces.append(location)
             index[word] = occurrenceces


#按照字母順序列出
for word in sorted(index,key=str.upper):
        print(word,index[word])
