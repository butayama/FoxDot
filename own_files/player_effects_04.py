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

p1 >> pluck([1,2,3,4,5,6,7,8,9,10,11,12])

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

var.chords = var([0,1,5,3],4)
p4 >> soprano(var.chords+[0,2,5,6], dur=8, oct=5, room=0.2, verb=0.2, amp=1)

p4.stop()

p5.stop()

p5 >> bell(var.chords+[0,2,5,6], dur=4, oct=4, echo=0.75, echotime=8, room=0.2, verb=0.2, spin=4, amp=1)

p6 >> gong(var.chords+[0,2,5,6], room=0.1, echo=0.75, echotime=4, dur=6, oct=3, verb=0.2, amp=1)

p6.stop()

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

d1 >> play("aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUv", dur=8, sus=12, room=0.5)

d1 >> play("aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUv", dur=8, sus=8, echo=0.5, room=0.5)

d1 >> play("aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUv", dur=8, sus=12, echo=0.75, room=0.5)

d1 >> play("aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUv", dur=8, sus=8, echo=0.9, room=0.5)

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

p1.stop()

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
d1 >> play("(aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUv)", dur=8, room=0.1, echo=0.75, echotime=2, lpf=linvar([1000,5000],16), sus=6, spin=3, amp=0.5)

d1 >> play("(aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUv)", dur=8, room=0.1, echo=0.75, echotime=2, sus=6, spin=2, amp=0.5)

d1 >> play("(aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUv)", dur=8, room=0.1, echo=0.75, echotime=2, sus=6, amp=0.5)

p1.stop()

# Move the pan left to right 4 times across 4 beats
p1 >> pads(dur=4, spin=4)

p1.stop()

d1.stop()

d1.stop()
var.chords = var([0,1,5,3],4)

# Move the pan left to right 4 times across 1 beat
p1 >> pads(dur=4, sus=6, spin=4)

# bells melodic
p5 >> bell(var.chords+[0,2,5,6], dur=4, oct=4, echo=0.75, echotime=8, room=0.2, verb=0.2, amp = 0.5, spin=4)

p5 >> gong(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(), room=0.1, echo=0.75, echotime=4, dur=6, oct=3, verb=0.2)

# synth melodic
p5 >> varsaw(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(16), dur=8, oct=5, room=0.2, verb=0.2)

p5 >> prophet(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=8, oct=4, room=0, verb=0)

p5 >> swell(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=8, oct=4, room=0, verb=0)

p5 >> razz(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=8, oct=4, room=0, verb=0)

p5 >> pasha(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=8, oct=4, room=0, verb=0)

# synth melodic + accords
p5 >> lazer(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(), dur=8, oct=5, room=0.2, verb=0.2)

p5 >> scatter(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(), dur=8, oct=5, room=0.2, verb=0.2)

# synth melodic + echoes
p5 >> charm(var.chords+[0,2,5,6], dur=8, oct=4, room=0.1, verb=0.1)

p5 >> soprano(var.chords+[0,2,5,6], dur=8, oct=5, room=0.2, verb=0.2)

# blubber melodic
p5 >> growl(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(), dur=8, oct=5, room=0.2, verb=0.2)

p5 >> space(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=8, oct=5, room=0, verb=0)

# synth melodic bass
p5 >> bass(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=8, oct=5, room=0.9, verb=0.5)

# bells melodic
p5 >> bell(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(), dur=8, oct=5, room=0.2, verb=0.2)

p5 >> gong(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(), dur=8, oct=3, room=0.2, verb=0.2)

# simple e-instrument melodic
p5 >> viola(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=8, oct=4, room=0, verb=0)

p5 >> blip(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=8, oct=4, room=0, verb=0)

p5 >> orient(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=8, oct=4, room=0, verb=0)

# simple e-instrument melodic + noise
p5 >> quin(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=dur=8, oct=4, room=0, verb=0)

p5 >> ripple(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=8, oct=4, room=0, verb=0)

p5 >> spark(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=8, oct=4, room=0, verb=0)

p5 >> zap(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=8, oct=4, room=0, verb=0)

p5 >> pulse(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=8, oct=4, room=0, verb=0)

# organ + noise melodic
p5 >> klank(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=8, oct=4, room=0, verb=0)

# organ melodic
p5 >> feel(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=8, oct=4, room=0, verb=0)

p5 >> ambi(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=8, oct=4, room=0, verb=0)

# organ melodic + echoes + accords
p5 >> glass(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=8, oct=4, room=0, verb=0)

# Xylophone melodic
p7 >> marimba(var.chords+[0,2,5,6] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)

# Xylophone melodic + noise
p8 >> snick(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)

p9 >> sinepad(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(16), dur=PDur([5,2,3],8), oct=5, room=0, verb=0)

# drums melodicMajor
p10 >> donk(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)

# piano melodic
p11 >> piano(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)

p5 >> keys(P[0,2,5,6, [(0, 2, 5), 9, 11, 12,(2, 4, 5, 8)]] + P[0,3, 4, 5].stutter(8), dur=PDur([5,2,3],8), oct=4, room=0, verb=0)
