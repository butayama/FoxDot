# https://foxdot.org/docs/player-attributes/


# http://studio.dubroom.org/tutorials-computerdub07.htm
# THE NYABINGHI RHYTHM

# include files:
# https://stackoverflow.com/questions/714881/how-to-include-external-python-code-to-use-in-other-files

import platform
h = platform.uname()[1]
print(h)
# Windows DESKTOP-0AVFOFJ
if h == "DESKTOP-0AVFOFJ": 
    with open(r'E:\GitHub\FoxDot\own_files\nyabinghi.py') as f: exec(f.read())
    with open(r'E:\GitHub\FoxDot\own_files\amp_list_dr_random_01.py') as f: exec(f.read())
    with open(r'E:\GitHub\FoxDot\own_files\amp_list_dr_random_02.py') as f: exec(f.read())
# Debian - akoya:
elif h == "akoya":    
    with open(r'/home/uwe/PycharmProjects/FoxDot/own_files/nyabinghi.py') as f: exec(f.read())
    with open(r'/home/uwe/PycharmProjects/FoxDot/own_files/amp_list_dr_random_01.py') as f: exec(f.read())
    with open(r'/home/uwe/PycharmProjects/FoxDot/own_files/amp_list_dr_random_02.py') as f: exec(f.read())


# include_message("Include function text from include_test loaded")
# print(message)

def csr(bpm=140, scale="chromatic",root="C"):
    Clock.bpm = bpm
    Scale.default = scale
    Root.default = root
    return

# _______________________________________________________________________________________________________
# start playing according to a planned scedule
# _______________________________________________________________________________________________________
csr()
number_of_song_measures = 128

notes_to_play = ("xabcdefghij")
   
def pluck_a_note(note_x="x"):
    p1 >> play(note_x,dur=4)

def song_init(init_time=Clock.now()):
    for i in range(0,10):
        x_time = init_time+i*4
        print(i, x_time)
        Clock.schedule(pluck_a_note, [Clock.now()+4], notes_to_play[i])

song_init(Clock.now())

Clock.set_time(6)
Clock.schedule(pluck_a_note, Clock.now()+4, notes_to_play[0])
print(Clock.now()+4)

def update(n=[0], symb="x"):
    print(n)
    if n[0] < 10:
        pluck_a_note(symb)
    else:
        p1.stop()
        return
    # Clock.future(4, update, [n + 1], notes_to_play[i])  
    n[0] += 1
    print(n)  
    Clock.future(1, update, n[0])

update()  

Clock.future(1, update, [1])

def update1(n=0):
    print(n)
    d1 >> play("x ")


Clock.future(1, update1, [3])

update1()
