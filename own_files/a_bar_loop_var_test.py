a = var([0,4,5,3],8)

a.update([1,4], 8)

c = linvar([0,1],16)

# a 'Pvar' is a 'var' that can store patterns (as opposed to say, integers)
d = Pvar([P[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], P[0, 1, 2, 3, 4, 5, 4, 3, 2, 1]], 8)

print(int(Clock.now()), d)

p1 >> bass(a, amp=c, dur=1/4) + d

Scale.default = Pvar([Scale.major, Scale.minor],16)

p1 >> play("x-o-", hpf=linvar([0,4000],[32,0]))

pattern1 = P[0, 1, 2, 3]
pattern2 = P[4, 5, 6, 7]

print(var([pattern1, pattern2], 4))

print(Pvar([pattern1, pattern2], 4))

p1 >> pluck(Pvar([pattern1, pattern2], 4), dur=1/4)

p1 >> pluck(var([pattern1, pattern2], 4), dur=1/4)

# Without a rest, 5 notes (yes, a dur=1 would work, but lets be explicit to counterpoint the next example)
p1 >> pads([0,1,2,3,4], dur=[1,1,1,1,1], start=4)

# With a rest ... 4 notes and a rest, note "4" is silenced for 4 beats
p1 >> pads([0,1,2,3,4], dur=[1,1,1,1,rest(4)])

print(Clock.now())

print(Clock.latency)
print(Clock.mod(32))

var.a = var(Clock.now() + 500)
print(var.a)
Clock.schedule(lambda: print(f"future{var.a}"), var.a) 

var.b = var(Clock.now() + 16)
print(var.b)
Clock.future(var.a, lambda: print("hello")) 

Clock.future(4, lambda: print("hello"))

# We can call something every n beats
Clock.every(8, lambda: print("hello"))

def change(a=0):
    if a == 0:
        p1 >> pluck(Pvar([pattern1, pattern2], 4), dur=1/4)
    if a == 4:
        p1 >> pluck(var([pattern1, pattern2], 4), dur=1/4)
        
change()   

Clock.every(64, lambda: change(0))
Clock.every(25, lambda: change(4))

# You can create your own function, and decorate it, to be able
# to use it in an .every on a Player object
@PlayerMethod
def test(self):
    print(self.degree)

p1 >> pluck([0,4]).every(4, "test")

# And cancel it with
p1.never("test")


###########################
# Offsetting the start time

# Another useful trick is offsetting the start time for the var. By
# default it is when the Clock time is 0 but you can specify a different
# value using the "start" keyword

print(linvar([0, 1], 8))
print(linvar([0, 1], 8, start=2))

# This can be combined with Clock.mod() to start a ramp at the start of the
# next 32 beat cycle:

d1 >> play("x-o-", hpf=linvar([0,4000],[32,inf], start=Clock.mod(32)))



a = var([0,4,5,3],8)
p1 >> pads(a, dur=1, amp=0.5).offbeat() + (0,2,4)
b1 >> bass(a, dur=1/4, sus=1, amp=0.5)


a = var([0,4,5,3],4)
p2 >> pads(a + var([4,[2,0],1] [2,1,1]), dur=[1/2,1/4,1/4]) + [0,[-1,1]]
v1 >> viola(a, dur=4) + (0,var([[9,2],4],4))
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

var.a = var([0, 3, 0, 4], var.b)

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
