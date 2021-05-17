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


#-----------------------------------------------------------------------------------------------------------
PLAYER EFFECTS
#-----------------------------------------------------------------------------------------------------------

# Slide effect added
p1 >> pluck(dur=4, slide=1, slidedelay=0.5)

# Slide effect not added
p1 >> pluck(dur=4, slide=0, slidedelay=0.5)

# Slide effect added, with zero delay
p1 >> pluck(dur=4, slide=1, slidedelay=0)


# One beat duration, half-beat duration
p1 >> pluck(dur=1, sus=1/2)

p1 >> pluck([0, 7, 6, 4, 2], dur=[6,5,4,3,2], sus=[4,4,1,2,3,4,5,6])

# Alternate between left, center, and right
p1 >> pluck(pan = [-1, 0, 1])

# Play two notes at the same time, but in different speakers
p1 >> pluck((0, 4), pan=(-1,1))

# Gradually move the sound's panning from left to right using a "linvar"
p1 >> pluck([0, 2, 4, 7], dur=1/4, pan=linvar([-1,1],8))

# Simple flanger effect
p1 >> pluck(fmod = 2)

# Vary the effect over time
p1 >> pluck(fmod=linvar([-10,10],8), dur=1/4, sus=1)

p1 >> pads(dur=4, vib=4)

p1 >> pads(dur=4, vib=4, vibdepth=0.1)

p1 >> pads(dur=4, vib=4, vibdepth=1)

# Slide one octave up
p1 >> pluck(dur=4, slide=1)

# Slide to 0
p1 >> pluck(dur=4, slide=-1)

# Delay the slide effect to start half way through the note
p1 >> pluck(dur=4, slide=0.5, slidedelay=0.5)

# Slide from one octave up
p1 >> pluck(dur=4, slidefrom=1)

# Slide from 0
p1 >> pluck(dur=4, slidefrom=-1)

# Delay the slide effect to start half way through the note
p1 >> pluck(dur=4, slidefrom=0.5, slidedelay=0.5)

# Bends one octave up and back again
p1 >> pluck(dur=4, bend=1)

# Bend to 0 and back again
p1 >> pluck(dur=4, bend=-1)

# Delay the bend effect to start half way through the note
p2 >> pluck(dur=4, slide=0.5, bend=0.5)

p1 >> pluck([0, 2, 4, 7], dur=8, slide=linvar([-1,1],0.1), bend=0.01)

# Chop a sound into 4 parts
p1 >> pluck([0,1,2,3], dur=4, chop=4)

# If the duration varies, the sizes of chop will vary too
p1 >> pluck([0,[4,6,7]], dur=PDur(3,8), chop=4)

# Changing a single value for "sus" evens out the sizes and creates a nice overlapping echo effect
p1 >> pluck([0,[4,6,7]], dur=PDur(3,8), chop=4, sus=2)

# Using chop
c1 >> play("C", dur=32, chop=16, coarse=0)

# Using coarse
c1 >> play("C", dur=32, coarse=16, chop=0)

b1 >> bass(dur=2, chop=4, coarse=0)

b1 >> bass(dur=2, coarse=4, chop=0)

# Set the high pass filter cutoff to 2000 Hz
d1 >> play("  o  ", hpf=2000)


#--------------------------------------------------------------------------------
# They'd be extinct
#--------------------------------------------------------------------------------
# Set the cutoff to change over time using a linvar
d1 >> play("  o  ", hpf=linvar([0,2000],32))


# Set the high pass filter cutoff to 2000 Hz
d1 >> play("  o  ", hpf=2000)

# Set the resonance to 0.2 - can you hear the difference?
d1 >> play("  o  ", hpf=2000, hpr=0.2)

# Set the cutoff *and* resonance to change over time using linvar
d2 >> play("  o  ", hpf=linvar([0,5000],64), hpr=linvar([1,0.1],28))



# Set the low pass filter cutoff to 400 Hz
d1 >> play("  o  ", lpf=400)

# Changing the resonance - can you hear the difference?
d1 >> play("  o  ", lpf=400, lpr=0.2)

# Use a linvar to vary both values over time
d1 >> play("aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUv", dur=8, lpf=linvar([1000,5000],32), lpr=linvar([0.5,0.1],28), slide=linvar([-0.1,1],0.1), bend=0.05, sus=2, room=0.8, mix=0.8)

d1 >> play("aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUv", dur=8, lpf=linvar([1000,5000],16), lpr=linvar([0.5,0.1],28), sus=12)

d1.stop()
p1.stop()

#--------------------------------------------------------------------------------

# Apply the bit-crusher effect
d1 >> play("aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUv", crush=8, lpf=linvar([1000,5000] ,16),sus=8)

# Reduce the number of bits for more distortion
d1 >> play("a a ", crush=4, bits=4)

# Or reduce the sample rate for a different style of distortion!
d1 >> play("a a ", crush=32, bits=8)

# Add distortion to both sample and synth players
d1 >> play("  o  ", hpf=linvar([0,5000],64), hpr=linvar([1,0.1],28), dist=0.2)

p1 >> dirt([0,5], dist=0.3, dur=8) + (0,4)

# Add distortion to both sample and synth players
d1 >> play("    o   ", shape=0.5)

p1 >> dirt([0,5], shape=0.5, dur=8) + (0,4)

# Add overdrive distortion
p1 >> dirt(dur=8, drive=0.1)

# Emulate playing the sounds in a small room
p1 >> play("a o ", room=0.25)

# Emulate playing the sounds in a larger room
p1 >> play("a o ", room=0.8)

# Make the signal more 'wet'
p1 >> play("aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUv", dur=8, lpf=linvar([1000,5000],32), lpr=linvar([0.5,0.1],28), room=0.8, mix=0.8)

p1 >> blip(dur=4, echo=1)

# We don't hear any echo effect
d1 >> play("a o ", dur=1, echo=0.75)

# Add reverb and we do
d1 >> play("aAbBcCdDeEfFgG", dur=8, echo=0.75, room=0.5)

# Only hear one echo
p1 >> blip(dur=4, echo=1)

# Now we hear several
p1 >> blip(dur=4, echo=1, echotime=8)

# We can use echo to make drum loops more interesting too
d1 >> play("(a o )(a o )o ", room=0.1, echo=0.75/2, echotime=4)

