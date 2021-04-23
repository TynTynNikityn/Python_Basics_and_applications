"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

Примечание:
Считать все строки по одной из стандартного потока ввода вы можете, например, так

import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line
"""
import sys
import re
pattern=r'cat.*cat'

for line in sys.stdin:
    line=line.strip()
    if re.findall(pattern,line):
        print(line)
"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.

Примечание:
Для работы со словами используйте группы символов \b и \B.
Описание этих групп вы можете найти в документации.
"""
import sys
import re
pattern=r'\bcat\b'

for line in sys.stdin:
    line=line.strip()
    if re.findall(pattern,line):
        print(line)

"""
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа."""
import sys
import re
pattern=r'z\w{3}z'

for line in sys.stdin:
    line=line.strip()
    if re.findall(pattern,line):
        print(line)

"""Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\﻿"."""
import sys
import re
pattern=r'\\'

for line in sys.stdin:
    line=line.strip()
    if re.findall(pattern,line):
        print(line)

"""
Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор
"""
import sys
import re
pattern=r'\b(\w+)\1\b'

for line in sys.stdin:
    line=line.strip()
    if re.findall(pattern,line):
        print(line)

"""
Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки."""

import sys
import re
pattern=r'human'

for line in sys.stdin:
    line=line.strip()
    print(re.sub(pattern,'computer',line))

"""
Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".

Примечание:
Обратите внимание на параметр count у функции sub."""
import sys
import re
pattern=r'\b[aA]+\b'

for line in sys.stdin:
    line=line.strip()
    print(re.sub(pattern,'argh',line, count=1))

"""
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w."""
import sys
import re
pattern=r'\b(\w)(\w)'

for line in sys.stdin:
    line=line.strip()
    print(re.sub(pattern,r'\2\1',line))

"""
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w."""
import sys
import re
pattern=r'(\w)\1{1,}'

for line in sys.stdin:
    line=line.strip()
    print(re.sub(pattern,r'\1',line))