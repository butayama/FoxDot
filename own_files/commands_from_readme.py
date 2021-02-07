print(1 + 1)

print(SynthDefs)

p1 = Player("p1")
p1 >> pads([0,1,2,3])
p1 >> pads([0,1,2,3], dur=[1/4,3/4], sus=1, vib=4, scale=Scale.minor)

p1 >> pads([(0,2,4),1,2,3], dur=[1/4,3/4], sus=1, vib=4, scale=Scale.minor)

p2 = Player("p2")
p1 >> pads([(0,2,4),1,2,3], dur=[1/4,3/4], sus=1, vib=4, scale=Scale.minor)

print(Samples)

d1 >> play("x-o-")
bd >> play("x( x)  ")
hh >> play("---[--]")
sn >> play("  o u ")
xx >> play("xx--oo-")

d1 >> play(P["x( x)  "].palindrome().zip("---[--]").zip(P["  o "].amen())) 

d1 >> play(P["x( x)  "].palindrome() & "---[--]" & P["  o "].amen())

d1 >> play("x-o{-[--]o[-o]}")

p1 >> play("|x2|-o-")

p1 >> play("|x[12]| o ")

p1 >> play("|x(12)| o ")

p1 >> play("|x{0123}| o ")

bd >> play("x o  xo ")

bd.shuffle()

bd.rotate()

bd >> play("x-o-[xx]-o(-[oo])").every([6,2], 'mirror').every(8, 'shuffle')



