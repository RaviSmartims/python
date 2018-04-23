Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> word = 'word'
>>> word
'word'
>>> sentence = "This is a sentence"
>>> sentence
'This is a sentence'
>>> paragraph = """This is a paragraph. It is made up of multiple lines and sentences""""
SyntaxError: EOL while scanning string literal
>>> paragraph = """This is a paragraph.It is made up of multiple lines and sentences""""
SyntaxError: EOL while scanning string literal
>>> paragraph = """This is a paragraph.It is made up of multiple lines and sent""""
SyntaxError: EOL while scanning string literal
>>> paragraph =
SyntaxError: invalid syntax
>>> paragraph = """This is a paragraph"""
>>> paragraph
'This is a paragraph'
>>> #!/usr/bin/python3 
input("\n\nPress the enter key to exit.")


Press the enter key to exit.
''
>>> #!/usr/bin/python3 
input("\n\nPress the enter key to exit.")


Press the enter key to exit.ravi
'ravi'
>>> input("\n\nPress the enter key to exit.")


Press the enter key to exit.ravi
'ravi'
>>> input("\nPress the enter key to exit.")

Press the enter key to exit.ravi
'ravi'
>>> input("Press the enter key to exit.")
Press the enter key to exit.ravi
'ravi'
>>> input("\n\nPress the enter key to exit.")


Press the enter key to exit.ravi reddy
'ravi reddy'
>>> input("Press the enter key to exit.")
Press the enter key to exit.ravi reddy
'ravi reddy'
>>> list = [ 'abcd', 786 , 2.23, 'john', 70.2 ] 
tinylist = [123, 'john']
SyntaxError: multiple statements found while compiling a single statement
>>> list
<class 'list'>
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
>>> print(list)
['abcd', 786, 2.23, 'john', 70.2]
>>> print(list[0])
abcd
>>> print (list[1:3])
[786, 2.23]
>>> print (list[2:])
[2.23, 'john', 70.2]
>>> print (tinylist * 2)
[123, 'john', 123, 'john']
>>> print (list + tinylist)
['abcd', 786, 2.23, 'john', 70.2, 123, 'john']
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
Traceback (most recent call last):
  File "C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py", line 5, in <module>
    dict['one'] = "This is one"
TypeError: 'type' object does not support item assignment
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
>>> print(dict['one'])
This is one
>>> print(dict[2])
This is two
>>> print(tinydict)
{'name': 'Ravi', 'code': 6784, 'dept': 'IOT'}
>>> print(tinydict.keys)
<built-in method keys of dict object at 0x00000022D16C3288>
>>> print(tinydict.keys())
dict_keys(['name', 'code', 'dept'])
>>> print(tinydict.values())
dict_values(['Ravi', 6784, 'IOT'])
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
Enter amount: 600
Discount 30.0
Net payable: 570.0
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
Enter amount: 600
Discount 30.0
Net payable: 600
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
Enter amount: 600
Discount 30.0
Net payable: 570.0
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
Enter amount: 4000
Discount 400.0
Net payable: 3600.0
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
Enter amount: 6000
Discount 900.0
Net payable: 5100.0
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
Enter amount: 12
Discount 0.6000000000000001
Net payable: 11.4
Enter the number:
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
Enter amount: 12
Discount 0.6000000000000001
Net payable: 11.4
Enter the number:
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
Enter amount: 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
Enter the number:12
Divisible by both number 3 and 2
>>> 8
8
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
Enter the number:9
Divisible by 3 not divisible by 2
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
Enter the number:11
Not divisible by both 2 and 3
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
Enter the number:5
Not divisible by both 2 and 3
Current Letter : P
Current Letter : y
Current Letter : t
Current Letter : h
Current Letter : o
Current Letter : n

Current fruit : banana
Current fruit : apple
Current fruit : mango
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
Enter the number:4
Divisible by 2 and not divisible by 3
Current Letter : P
Current Letter : y
Current Letter : t
Current Letter : h
Current Letter : o
Current Letter : n

Current fruit : banana
Current fruit : apple
Current fruit : mango
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
Enter the number:4
Divisible by 2 and not divisible by 3
Current Letter : P
Current Letter : y
Current Letter : t
Current Letter : h
Current Letter : o
Current Letter : n

Current fruit : banana
Current fruit : apple
Current fruit : mango
The list contains the odd numbers
The list contains the odd numbers
The list contains the odd numbers
The list contains the odd numbers
The list contains the odd numbers
The list contains the odd numbers
The list contains the odd numbers
The list contains the odd numbers
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
Enter the number:1
Not divisible by both 2 and 3
Current Letter : P
Current Letter : y
Current Letter : t
Current Letter : h
Current Letter : o
Current Letter : n

Current fruit : banana
Current fruit : apple
Current fruit : mango
The list contains the odd numbers
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
Enter the number:1
Not divisible by both 2 and 3
Current Letter : P
Current Letter : y
Current Letter : t
Current Letter : h
Current Letter : o
Current Letter : n

Current fruit : banana
Current fruit : apple
Current fruit : mango
The list contains the even numbers
The list contains the odd numbers
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
The list contains the even numbers
The list contains the odd numbers
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
1
2
3
4
5
6
7
8
9
10
2
4
6
8
10
12
14
16
18
20
3
6
9
12
15
18
21
24
27
30
4
8
12
16
20
24
28
32
36
40
5
10
15
20
25
30
35
40
45
50
6
12
18
24
30
36
42
48
54
60
7
14
21
28
35
42
49
56
63
70
8
16
24
32
40
48
56
64
72
80
9
18
27
36
45
54
63
72
81
90
10
20
30
40
50
60
70
80
90
100
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
1
2
3
4
5
6
7
8
9
10
2
4
6
8
10
12
14
16
18
20
3
6
9
12
15
18
21
24
27
30
4
8
12
16
20
24
28
32
36
40
5
10
15
20
25
30
35
40
45
50
6
12
18
24
30
36
42
48
54
60
7
14
21
28
35
42
49
56
63
70
8
16
24
32
40
48
56
64
72
80
9
18
27
36
45
54
63
72
81
90
10
20
30
40
50
60
70
80
90
100

>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
1

2

3

4

5

6

7

8

9

10

2

4

6

8

10

12

14

16

18

20

3

6

9

12

15

18

21

24

27

30

4

8

12

16

20

24

28

32

36

40

5

10

15

20

25

30

35

40

45

50

6

12

18

24

30

36

42

48

54

60

7

14

21

28

35

42

49

56

63

70

8

16

24

32

40

48

56

64

72

80

9

18

27

36

45

54

63

72

81

90

10

20

30

40

50

60

70

80

90

100

>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
1
2
3
4
5
6
7
8
9
10
2
4
6
8
10
12
14
16
18
20
3
6
9
12
15
18
21
24
27
30
4
8
12
16
20
24
28
32
36
40
5
10
15
20
25
30
35
40
45
50
6
12
18
24
30
36
42
48
54
60
7
14
21
28
35
42
49
56
63
70
8
16
24
32
40
48
56
64
72
80
9
18
27
36
45
54
63
72
81
90
10
20
30
40
50
60
70
80
90
100
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
12345678910
2468101214161820
36912151821242730
481216202428323640
5101520253035404550
6121824303642485460
7142128354249566370
8162432404856647280
9182736455463728190
102030405060708090100
>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
1
2
3
4
5
6
7
8
9
10

2
4
6
8
10
12
14
16
18
20

3
6
9
12
15
18
21
24
27
30

4
8
12
16
20
24
28
32
36
40

5
10
15
20
25
30
35
40
45
50

6
12
18
24
30
36
42
48
54
60

7
14
21
28
35
42
49
56
63
70

8
16
24
32
40
48
56
64
72
80

9
18
27
36
45
54
63
72
81
90

10
20
30
40
50
60
70
80
90
100

>>> 
======= RESTART: C:/Users/Ravireddy Jerru/Desktop/python/04_20_2018.py =======
1 2 3 4 5 6 7 8 9 10 
2 4 6 8 10 12 14 16 18 20 
3 6 9 12 15 18 21 24 27 30 
4 8 12 16 20 24 28 32 36 40 
5 10 15 20 25 30 35 40 45 50 
6 12 18 24 30 36 42 48 54 60 
7 14 21 28 35 42 49 56 63 70 
8 16 24 32 40 48 56 64 72 80 
9 18 27 36 45 54 63 72 81 90 
10 20 30 40 50 60 70 80 90 100 
>>> 
