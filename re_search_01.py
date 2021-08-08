#search for lines that conain 'From'
import re,  urllib.request

from urllib.request import Request, urlopen

# get the example text file from the web
url = "https://www.py4e.com/code3/mbox-short.txt"
# hand = urllib.request.urlopen(url)
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read().decode('utf-8')
count = 0
hand = webpage.split('\n')

# find all lines that start with From: and have a '@' character in them
for line in hand:
  line = line.rstrip()
  if re.search('^From:.+@', line):
    count += 1
    print(line)
print(count)

# [a-zA-Z0-9] - match ranges of chars in brackets, \S* - match zero or more non-whitespace
mail_adresses_lst = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',webpage)
print(mail_adresses_lst) 

# find all lines that start with X followed by zero or more non-whitespace chars followed by a column,
# get the number
for line in hand:
  line = line.rstrip()
  x = re.findall('^X\S*: ([0-9.]+)', line)
  if len(x) > 0:
    count += 1
    print(x)
print(count)

# find all revisoin numbers
for line in hand:
  line = line.rstrip()
  x = re.findall('rev=([0-9.]+)', line)
  if len(x) > 0:
    count += 1
    print(x)
print(count)

# get help for regular expressions
dir(re)
help(re.search)