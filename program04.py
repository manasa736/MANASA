Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from math import sqrt.gcd
SyntaxError: invalid syntax

================================ RESTART: Shell ================================
from math import sqrt,gcd
sqrt(2)
1.4142135623730951
gcd(24,40)
8

================================ RESTART: Shell ================================
from math import*
sqrt(2)
1.4142135623730951
gcd(24,40)
8

================================ RESTART: Shell ================================
import math
math.sqrt(2)
1.4142135623730951
math.gcd(24,40)
8

================================ RESTART: Shell ================================
import math as m
m.sqrt(4)
2.0
m.gcd(24,50)
2
m.trunc(4,5)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    m.trunc(4,5)
TypeError: math.trunc() takes exactly one argument (2 given)
m.trunc(4.5)
4
m.floor(9.4)
9
m.ceil(4,8)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    m.ceil(4,8)
TypeError: math.ceil() takes exactly one argument (2 given)
m.ceil(4.8)
5
m.log(1024.2)
6.93166709902845
m.log(1024,2)
10.0
m.ceil(9.1)
10
pi=3.14159
r=2.5
h=10**0.5
volume=pi* r**2 *h
printpi=3.14159


========================================================= RESTART: Shell ========================================================
print('{0},{1},{2}'.format('apple', 'banana', 'carrot', 'pen'))
apple,banana,carrot
print('{0},{0}{0},{1},{2}'.format('apple', 'banana', 'carrot', 'pen'))
apple,appleapple,banana,carrot
print('{0},{0},{3},{1},{2}'.format('apple', 'banana', 'carrot', 'pen'))
apple,apple,pen,banana,carrot
print('{0},{1},{2},{0},{3},{1},{2}'.format('apple', 'banana', 'carrot', 'pen'))
apple,banana,carrot,apple,pen,banana,carrot
print('{0}{1}{2}{0}{3}{1}{2}'.format('apple', 'banana', 'carrot', 'pen'))
applebananacarrotapplepenbananacarrot

==================================== RESTART: C:/Users/User/Desktop/python/day6/program05.py ====================================
apple,banana,carrot
apple,appleapple,banana,carrot
apple,apple,pen,banana,carrot
apple,banana,carrot,apple,pen,banana,carrot
applebananacarrotapplepenbananacarrot

========================================================= RESTART: Shell ========================================================
print('{}, {}, {}'.format('apple', 'banana', 'carrot'))
apple, banana, carrot
print('gangully purchased a kg of {},a dozen of {}and half kg of {]'.format('apple', 'banana', 'carrot'))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print('gangully purchased a kg of {},a dozen of {}and half kg of {]'.format('apple', 'banana', 'carrot'))
ValueError: expected '}' before end of string
print('gangully purchased a kg of {},a dozen of {}and half kg of {]'.format('apple', 'banana', 'carrot'))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print('gangully purchased a kg of {},a dozen of {}and half kg of {]'.format('apple', 'banana', 'carrot'))
ValueError: expected '}' before end of string
print('{}, {}, {}'.format('apple', 'banana', 'carrot'))
apple, banana, carrot
print('gangully purchased a kg of {},a dozen of {}and half kg of {}'.format('apple', 'banana', 'carrot'))
gangully purchased a kg of apple,a dozen of bananaand half kg of carrot
print('gangully purchased a kg of {},a dozen of {} and half kg of {}'.format('apple', 'banana', 'carrot'))
gangully purchased a kg of apple,a dozen of banana and half kg of carrot

==================================== RESTART: C:/Users/User/Desktop/python/day6/program06.py ====================================
apple, banana, carrot
gangully purchased a kg of apple,a dozen of bananaand half kg of carrot
gangully purchased a kg of apple,a dozen of banana and half kg of carrot
print('{2}, {1}, {0}'.format('apple', 'banana', 'carrot'))
carrot, banana, apple
print('{2}, {1}, {1}, {0}'.format('apple', 'banana', 'carrot'))
carrot, banana, banana, apple
print('{2}, {1}, {0}'.format(*'abcd'))
c, b, a
x,*y,z='computer'
x
'c'
z
'r'
y
['o', 'm', 'p', 'u', 't', 'e']
*x,y='abcd'
x
['a', 'b', 'c']
y
'd'
print('coordinates: {latitude}, {latitude}'.format(latitude='37.24N', longitude='-115.81W'))
coordinates: 37.24N, 37.24N
print('welcome :(name), your college is: {college}'.format(name='manasa', college='MTICA'))
welcome :(name), your college is: MTICA
>>> print('welcome :{name}, your college is: {college}'.format(name='manasa', college='MTICA'))
welcome :manasa, your college is: MTICA
>>> print('coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
coordinates: 37.24N, -115.81W
>>> student={24:'manasa',23:'joshna')
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> student={24:'manasa',23:'joshna'}
>>> type(student)
<class 'dict'>
>>> student
{24: 'manasa', 23: 'joshna'}
>>> student.keys()
dict_keys([24, 23])
>>> student.values()
dict_values(['manasa', 'joshna'])
>>> type(coord)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    type(coord)
NameError: name 'coord' is not defined
>>> coord = (3, 5)
>>> abc=(2,9)
>>> type(coord)
<class 'tuple'>
>>> type(abc)
<class 'tuple'>
>>> abc[0]
2
>>> print('x: {0[0]}; y:{0[1]};abc :[1[0]},{1[1]}'.format(coord,abc))
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print('x: {0[0]}; y:{0[1]};abc :[1[0]},{1[1]}'.format(coord,abc))
ValueError: Single '}' encountered in format string
>>> print('x: {0[0]}; y:{0[1]};abc :{1[0]},{1[1]}'.format(coord,abc))
x: 3; y:5;abc :2,9
