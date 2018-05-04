Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> re.match("c","a,b,c,d,e,f")
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    re.match("c","a,b,c,d,e,f")
NameError: name 're' is not defined
>>> re.match("c", "abcdef")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    re.match("c", "abcdef")
NameError: name 're' is not defined
>>> re.search("c","abcdef")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    re.search("c","abcdef")
NameError: name 're' is not defined
>>> import re
>>> re.search("c","abcdef")
<_sre.SRE_Match object; span=(2, 3), match='c'>
>>> re.match("c","abcdef")
>>> bool(re.match("c","abcdef"))
False
>>> re.search("c","abcdef\nc")
<_sre.SRE_Match object; span=(2, 3), match='c'>
>>> re.search("c","abdef\nc")
