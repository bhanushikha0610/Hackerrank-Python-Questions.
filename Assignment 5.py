#!/usr/bin/env python
# coding: utf-8

# # 1 Re split

# In[ ]:


regex_pattern =r"[.,]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))


# # 2 Group(), Groups() & Groupdict()
# 
# 

# In[ ]:


import re
string = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(string.group(1) if string else -1)

    


# # 3 Re.findall() & Re.finditer()

# In[ ]:


import re
vowel = "aeiou"
cons = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (cons, vowel, cons), input(), flags = re.I)
print('\n'.join(m or ['-1']))


# ## 4 Re.start() & Re.end()

# In[ ]:


import re

string = input()
substring = input()

pattern = re.compile(substring)
match = pattern.search(string)

if not match: 
    print('(-1, -1)')
    
while match:
    print('({0}, {1})'.format(match.start(), match.end() - 1))
    match = pattern.search(string, match.start() + 1)


# ## Regex Substitution

# In[ ]:


import re

for _ in range(int(input())):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))


# ## Validating phone numbers

# In[ ]:


import re

N = int(input())

for i in range(N):
    number = input()
    if(len(number)==10 and number.isdigit()):
        output = re.findall(r"^[789]\d{9}$",number)
        if(len(output)==1):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")


# ## Validating and Parsing Email Addresses

# In[ ]:


import re
n = int(input())
for _ in range(n):
    x, y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
        print(x,y)


# ## Hex Color Code

# In[ ]:


import re

T = int(input())
in_css = False
for _ in range(T):
    s = input()
    if '{' in s:
        in_css = True
    elif '}' in s:
        in_css = False
    elif in_css:
        for color in re.findall('#[0-9a-fA-F]{3,6}', s):
            print(color)


# ## HTML Parser - Part 1

# In[ ]:


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ('Start :', tag)
        for ele in attrs:
            print ('->', ele[0], '>', ele[1])

    def handle_endtag(self, tag):
        print ('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print ('Empty :', tag)
        for ele in attrs:
            print ('->', ele[0], '>', ele[1])

parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())


# ## HTML Parser - Part 
# 

# In[ ]:


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  
  
  
  
  
  
  

    # HTML Parser - Part 2 in Python - Hacker Rank Solution START
    def handle_comment(self, data):
        if (len(data.split('\n')) != 1):
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data.replace("\r", "\n"))
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)
    

  
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# ## Detect HTML Tags, Attributes and Attribute Values

# In[ ]:


from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]
        
html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# ## Validating UID

# In[ ]:


import re

for i in range(int(input())):
    N = input().strip()
    if N.isalnum() and len(N) == 10:
        if bool(re.search(r'(.*[A-Z]){2,}',N)) and bool(re.search(r'(.*[0-9]){3,}',N)):
            if re.search(r'.*(.).*\1+.*',N):
                print('Invalid')
            else:
                print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')


# ## Validating Credit Card Numbers

# In[ ]:


import re
for i in range(int(input())):
    S = input().strip()
    pre_match = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$',S)
    if pre_match:
        processed_string = "".join(pre_match.group(0).split('-'))
        final_match = re.search(r'(\d)\1{3,}',processed_string)
        if final_match:
            print('Invalid')
        else :
            print('Valid')
    else:
        print('Invalid')


# ## Validating Postal Codes

# In[ ]:


regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# ## Matrix Script

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
matrix = list(zip(*matrix))

sample = str()

for words in matrix:
    for char in words:
        sample += char
       
print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', sample)) 

