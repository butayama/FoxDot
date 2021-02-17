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

