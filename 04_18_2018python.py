Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str1 = "hi this is Ravi"
>>> str1.capitalize()
'Hi this is ravi'
>>> str1 = """ Tom is a good guy
Tom is hardworking
Tom is honest
Tom is a team player
Tom is a party pooper
Tom sleeps early
Tom works out """
>>> str1
' Tom is a good guy\nTom is hardworking\nTom is honest\nTom is a team player\nTom is a party pooper\nTom sleeps early\nTom works out '
>>> str1.count(Tom)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    str1.count(Tom)
NameError: name 'Tom' is not defined
>>> str1.count("Tom")
7
>>> str1 = "i lovetennis.com"
>>> str1.endswith(".com")
True
>>> str1.endswith(".org")
False
>>> str1 = "Catch me if you can"
>>> str1.find("you")
12
>>> str1.find("along")
-1
>>> str1 = "Hello World"
>>> str1.islower()
False
>>> str1="hello world"
>>> str1.islower()
True
>>> len(str1)
11
>>> str1 = "!!!!!!!! What's up buddy?"
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> str1 = "!!!!!!!! What's up buddy?"
>>> str1.lstrip("!")
" What's up buddy?"
>>> str1 = "Fox is king of the forest"
>>> str1
'Fox is king of the forest'
>>> str1.replace('Fox','Lion')
'Lion is king of the forest'
>>> str1 = "Tom Cruise"
>>> str1.spilt()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    str1.spilt()
AttributeError: 'str' object has no attribute 'spilt'
>>> str1.split()
['Tom', 'Cruise']
>>> 
