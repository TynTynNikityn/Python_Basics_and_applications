"""
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa
"""
count=0
s,t=(str(input()) for i in range(2))
for i in range(len(s)):
    a=s.startswith(t,i)
    if a:
        count+=1
print(count)