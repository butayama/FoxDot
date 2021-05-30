# Example 1
# ---------

when(lambda: 5 < 10:
    print(True)
else:
    print(False)

print True

# Example 2
# ---------        
a = 15
b = 10

if a > b:
    print("a is bigger")
else:
    print("b is bigger")

# This is how to 'stop' the statement above

__when__(lambda: a > b).remove()

# This removes *all* currently running when statements

__when__.reset()

help(when)

when(15 < 10)
print("a is bigger")


var.b = var([1,2,3,2,1], 1)

var.a = var([0, 3, 0, 4], 4)

p1 >> pluck(var.a, dur=[1,1/4,1/4,1/2,2]) + (0, 2, 4, 6)

p1 >> pluck(P[0, 3, 0, 4].stutter(32), dur=1/4) + (0, 2, 4)

# --------------------------------------------------------------------------------------------------------------
FoxDot v.0.8.11 on Windows
Python 3.9

if I follow the Example 1 in **foxdot_when_statement.py** using parenthesis with the print command: 
```
when 5 < 10:
    print(True)
else:
    print(False)

print True
```
I get the following SyntaxError:
```
>>> when 5 < 10:
...     print(True)
... else:
...     print(False)
Traceback (most recent call last):
  File "e:\github\foxdot\FoxDot\lib\Code\main_lib.py", line 155, in __call__
    exec(self._compile(code), self.namespace)
  File "e:\github\foxdot\FoxDot\lib\Code\main_lib.py", line 106, in _compile
    return compile(str(CodeString(string)), "FoxDot", "exec")
  File "FoxDot", line 1
    when 5 < 10:
         ^
SyntaxError: invalid syntax
```
if I replace "when" with "if" I get the expected result:
```
>>> if 5 < 10:
...     print(True)
... else:
...     print(False)
True
```

Same with Example 2.

if I try:
`__when__(lambda: a > b).remove()`
```
>>> __when__(lambda: a > b).remove()
Traceback (most recent call last):
  File "e:\github\foxdot\FoxDot\lib\Code\main_lib.py", line 155, in __call__
    exec(self._compile(code), self.namespace)
  File "FoxDot", line 2, in <module>
NameError: name '__when__' is not defined
```
same error message with:
`__when__.reset()`
>>> __when__.reset()
```
Traceback (most recent call last):
  File "e:\github\foxdot\FoxDot\lib\Code\main_lib.py", line 155, in __call__
    exec(self._compile(code), self.namespace)
  File "FoxDot", line 1, in <module>
NameError: name '__when__' is not defined
```

# --------------------------------------------------------------------------------------------------------------

print(PatternMethods)

help(__when__)

help(when)
