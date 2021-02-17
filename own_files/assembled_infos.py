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
