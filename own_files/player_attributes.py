# https://foxdot.org/docs/player-attributes/

print(Player.get_attributes())

p1 >> pluck([0, 1, 2, 3], dur=1/2, sus=2)

# Single value for all notes
p1 >> pluck([0, 1, 2, 3], dur=1/2)

# A list of durations can be integers, fractions, or floating point values
p1 >> pluck([0, 1, 2, 3], dur=[1, 1/2, 0.5])

p1 >> pluck([0, 1, 2, 3], dur=[0.1, 0.3, 0.43, 0.17])

# Skip every 3rd note
p1 >> pluck([0, 1, 2, 3], dur=[1, 1, 0])

# Rest every 3rd note for 2 beats
p1 >> pluck([0, 1, 2, 3], dur=[1, 1, rest(2)])

print(Scale.names())

# Play the major scale by default
p1 >> pluck([0, 2, 4, 6, 7])

# Change to minor
p1 >> pluck([0, 2, 4, 6, 7], scale=Scale.minor)

# Start a player in the default scale (Major)
p1 >> pluck([0, 2, 4, 6, 7])

# Change the default scale to Dorian
Scale.default = Scale.dorian

# You can specify the default scale as a string
Scale.default = "dorian"

p1 >> pluck([0, 1, 2], dur=[1, 1/2, 1/2], amp=[1, 0.5, 1/3])

# We can create quite rhythmic patterns using amp by using values of 0 as well:
p1 >> pluck(
      dur=1/4, 
      amp=[1, 1/2, 1/2, 1, 0, 1, 0, 1, 1/2, 1/2, 1, 0, 1, 1/2, 1/4, 1]
)

# Before a sound gets triggered by a player, the amp value is multiplied by amplify so that you can use things like TimeVar 
# to set an amplitude to be 1 or 0 (i.e. on and off) for certain amount of time:
    
p1 >> pluck(
      dur=1/4, 
      amp=[1, 1/2, 1/2, 1, 0, 1, 0, 1, 1/2, 1/2, 1, 0, 1, 1/2, 1/4, 1], 
      amplify=var([1,0],[6,2])
)

# Plays at the Clock.bpm tempo (default 120)
p1 >> pluck([0, 1, 2, 3])

# Force player to use 100 bpm
p2 >> bell([4, 5, 7], bpm=100)

# It will always play at 100 bpm even if Clock.bpm is changed
Clock.bpm = 200

# Default samples
p1 >> play("a A ")

# A different set of samples
p1 >> play("a A ", sample=1)

# Can be a list of values
p1 >> play("a A ", sample=[0, 1, 2])

# "Stutter" every third note
p1 >> pluck([0, 1, 2, 3], delay=[0, 0, (0, 0.5)])

# Delay a note to play *after* the following one
p1 >> pluck([0, 1, 2, 3], delay=[0, 0, (0, 1.5)])

# Change the root every 8 beats
p1 >> blip([0, 7, 6, 4, 2], dur=1, sus=2, root=var([0, 2, 4, 5], 8))

