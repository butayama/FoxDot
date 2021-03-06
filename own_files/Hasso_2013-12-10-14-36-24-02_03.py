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

p2 >> pluck(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(16), dur=PDur([5,2,3],8), oct=4)

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

p2 >> pluck(PTri(var([4,8],8)), dur=PDur(var([1/2,1/4,1/8],8))) 

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

p1 >> play("(a-2-b-c-dx3xe-**f-+g!-h1)(-o-x)", dur=1, sample=[0,1], room=0.9, verb=0.2, delay=(0,0.25))

p1 >> play("{a--bxxc==d++e--f**gooh}(x-o-o)", dur=1, room=0.9, sample=[1], verb=0.2, delay=(0,0.25))

p1 >> play("x-o-o{abcdefgh}(2x3x-**-+!-1)(x-o o[xo])", dur=1, sample=[0], room=0.9, verb=0.2, delay=(0,0.25))

p2 >> pluck(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(16), dur=PDur([5,2,3],8), oct=4, room=0.7, verb=0.5)
p2.stop()

p1 >> varsaw("x-o-o{abcdefgh}(2x3x-**-+!-1)(x-o o[xo])", dur=1, sample=[0], room=0.9, verb=0.2, delay=(0,0.25))

help(Samples)

p4 >> play("E:\GitHub\FoxDot\FoxDot\snd\_loop_\foxdot.wav")


p5 >> noise(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(16), dur=PDur([5,2,3],8), oct=5, room=0, verb=0)
p5 >> dab(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(), dur=PDur([5,2,3],8), oct=5, room=0.2, verb=0.2)
p5 >> varsaw(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(16), dur=PDur([5,2,3],8), oct=5, room=0.2, verb=0.2)
p5 >> lazer(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(), dur=PDur([5,2,3],8), oct=5, room=0.2, verb=0.2)
p5 >> growl(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(), dur=PDur([5,2,3],8), oct=5, room=0.2, verb=0.2)
p5 >> bass(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=5, room=0.9, verb=0.5)
p5 >> dirt(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(), dur=PDur([5,2,3],8), oct=5, room=0.2, verb=0.2)
p5 >> crunch(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(), dur=PDur([5,2,3],8), oct=4, room=0.9, verb=0.2)
p5 >> rave(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(), dur=PDur([5,2,3],8), oct=5, room=0.2, verb=0.2)
p5 >> scatter(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(), dur=PDur([5,2,3],8), oct=5, room=0.2, verb=0.2)
p5 >> charm(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0.1, verb=0.1)
p5 >> bell(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(), dur=PDur([5,2,3],8), oct=5, room=0.2, verb=0.2)
p5 >> gong(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(), dur=PDur([5,2,3],8), oct=3, room=0.2, verb=0.2)
p5 >> soprano(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(), dur=PDur([5,2,3],8), oct=5, room=0.2, verb=0.2)
p5 >> dub(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(16), dur=PDur([5,2,3],8), oct=7, room=0.3, verb=0.3)
p5 >> viola(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> scratch(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> klank(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> feel(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> glass(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> soft(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=3, room=0.2, verb=0.5)
p5 >> quin(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> pluck(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> spark(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> blip(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> ripple(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> creep(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> orient(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> zap(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> marimba(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> fuzz(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> bug(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> pulse(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> saw(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> snick(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> twang(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> karp(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(4), dur=PDur([5,2,3],8), oct=3, room=0.5, verb=0.5)
p5 >> arpy(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> nylon(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> donk(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> squish(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> swell(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> razz(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> sitar(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> star(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> jbass(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> piano(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> sawbass(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=5, room=.5, verb=.9)
p5 >> prophet(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> pads(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> pasha(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> ambi(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> space(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=3, room=0, verb=0)
p5 >> keys(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
p5 >> dbass(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=5, room=.5, verb=.2)
p5 >> sinepad(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(16), dur=PDur([5,2,3],8), oct=5, room=0, verb=0)

