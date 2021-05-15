rongsinator = SynthDef("rongsinator")

p1 >> rongsinator()

p1 >> rongsinator([0,2,4], damping=0.45, brightness=0.4, dur=[3], lin=inf, amp=[0.2/0.2/0.5], cosFreq=0.1, modeNum=3)
