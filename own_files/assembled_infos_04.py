# create a new player objetc
foo = Player()
foo >> pluck((3,5,8))

p1 >> pluck(1)

p1 >> pluck([0, 2, 4, 5, 7, 9, 11])

# More generally, all the lists are traversed regardless of their length.
p1 >> pluck([0,2,4], dur=[1,2], amp=[1,2,3,1,5])

# chords in round brackets ()
p1 >> pluck([0, 2, 4, 5, 7, 9, 11,(0, 2, 4, 5, 7, 9, 11)]) 

# nested lists

p1 >> pluck([0, 2, 4, 5, 7, 9, 11,[0, 2, 4, 5, 7, 9, 11]]) 
# plays 0, 2, 4, 5, 7, 9, 11, 0
#       0, 2, 4, 5, 7, 9, 11, 2
#       0, 2, 4, 5, 7, 9, 11, 4 ....

print(SynthDefs)

# define octave
p2 >> blip(oct=2)

# durations
p2 >> blip(oct=11,dur=[1/2,0.5,1,1,2, .5, .1, .2, .3, .4, .5])

print(Clock)

print(Scale.names())

p3 >> play("xxxx{[111]([-abc][de])}")

print(Player.Attributes())

help(Pattern)

print( P[1,2,3,4].stretch(10))

help(Patterns.Sequences)

pat = PBern(size=16, ratio=0.5)

a=(PEuclid2(5,13,'-', 'o'))
p2 >> play(a)

b=(PEuclid2(7,15,'x', 'o'))
p3 >> play(b)

c=(PEuclid2(5,17,'o', '-'))
p4 >> play(a)

p1 >> pluck(PTri(10), dur=1/2)

p1 >> pluck(0, dur=PDur([5,1,3],8))

p1 >> pluck(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(16), dur=PDur([5,2,3],8), oct=4)

p1 >> pluck(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + var([0,3],8), dur=PDur([5,2,3],8), oct=4)

a = var([0,1,2,3],[4,2,1,1])
b1 >> bass(a, dur=[1/2,1/2,1/4])

var.chords = var([0,4,7,3],4)
var.chords = var([0,1,5,3],4)
var.chords = var([0],1)

p1 >> pluck(var.chords + [0, 2, 4], dur=PDur([3,5,7],8))
b1 >> bass(var.chords, dur=[1/2,1/2,1/4])

p1 >> pluck(dur=PDur(var([3,5],4),8))

print(PDur(var([3,5],4),8))

p1 >> pluck(PTri(var([4,8],8)), dur=PDur(var([1/2,1/4,1/8],8))) 

p1 >> pluck(PTri(var([4,8,5],8,5)), dur=PDur(var([3,5],4),8)) 

Clock

p1 >> pluck(var.chords + [0, 2, 4], dur=PDur([3,5,7],8))

p1.every(8, "reverse")

p1.stop_calling("reverse")

p1.every(4, "stutter", oct=4, pan=[-0.5, 0.5])



Clock.schedule(lambda: p1.solo())
Clock.every(4, lambda: p1.solo())

p1 >> pluck(var.chords + [0, 2, 4], dur=PDur([3,5,7],8))
b1 >> bass(var.chords, dur=[1/2,1/2,1/4])

def add(a, b):
    print(a + b)
    a = a* 2
    b = b / 2
    Clock.schedule(add, beat=Clock.now() + 2, args=(a,b))
    
add(10,10)


p1 >> play("x-o{(xx-z)(-[xx])(z[0o])(-o-)}([1,z,2],z,3,!,t,z)", sample=[0,1,2,8])
p2 >> play("x-o{(xx-z)(-[xx])(z[0o])(-o-)}([1,z,2],z,3,!,t,z)", sample=[0,7,8])

print(P[0,1,2] & P[3,4])

print(P[0,1,2] & P[3,4])

p1 >> play(P["x-o-xo(xx-z)(-[xx])(z[0o])"] & P["(-o-)[({[1,z,2],[z,3],([!,t],z)})]"], sample=[0,1])

p1 >> play(P["x-o-x-=(-o3), -!zz"] & P[" *[**][*][o-]"], sample=[0,1], room=0.9, verb=0.2, hpf=20, chop=2) 

p1 >> play("x-o[--]", rate=((0.9,1),),pan=((-0.5,0.5),), delay=(0,0.25))

b=(PEuclid2(7,15,'a', 'b'))
p3 >> play(b)

p1 >> play("a-b-c-d-e-f-g-h")

