print(Samples)

p1 >> play("!#$%&*+-/1pppppp2pppppp3pppppp4:=@ABCDEFGHIJKLMNOPQRSTUVWXYZ\\^abcdefghijklmnopqrstuvwxyz~ACACCAppAAppppppA--oxAA")
p2 >> play("ACACCAppAAppppppA--oxAA")
p3 >> play("/1ABCDEFG2ABCDEFG3ABCDEFG4:=@ABC")
p4 >> play("!--oxAA")
p5 >> play("!\\^abcde\\~ACA\\CCAppAA\\ppppppA\\--oxAA")
p6 >> play("!F^abcdefFFFoooCCApFFpp---ooppA\\--oxAA")

p3.stop()
p1.stop()
p2.stop()
p4.stop()
p5.stop()
p6.stop()

p6 >> play("ox-xo--{(--ox)[1xx--x--](xx--xx)[xx--x--4]}(o0+--o)")

p1 >> pluck([0,2,4,5,7,9,(0,2,4,5),(0,1,4,7)])

d1 >> play(P["x-o-"].amen())

p5 >> pluck(P[0,1,2,4,6,8,P/(4,5,8),2,7,8,9], dur=1)

d1.stop()

pitches = P[0,1,2,3,4]
harmony = pitches + 2

p1 >> pluck(pitches)
p2 >> star(harmony)

p2 >> star(harmony, dur=1/2)

p3 >> star(dur=4).follow(p1) + 5

p2 >> star(dur=p1.dur).follow(p1) + 2

p4 >> dab(dur=2).follow(p1) + 4

p5 >> varsaw(dur=4).follow(p1) + 5


