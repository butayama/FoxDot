# hello_FoxDot.py
# example from readme.md

from FoxDot import *

synth_defs = {
    # 'loop':    loop,
    # 'stretch': stretch,
    # 'play1':   play1,
    # 'play2':   play2,
    # 'audioin': audioin,
    'noise':   noise,                                 
    'dab':     dab,                                 
    'varsaw':  varsaw,                                 
    'lazer':   lazer,                                 
    'growl':   growl,                                
    'bass':    bass,                                 
    'dirt':    dirt,                                 
    'crunch':  crunch,                                 
    'rave':    rave,                                 
    'scatter': scatter,                                 
    'charm':   charm,                                 
    'bell':    bell,                                 
    'gong':    gong,                                 
    'soprano': soprano,                                 
    'dub':     dub,                                
    'viola':   viola,                                 
    'scratch': scratch,                                 
    'klank':   klank,                                 
    'feel':    feel,                                 
    'glass':   glass,                                 
    'soft':    soft,                                 
    'quin':    quin,                                 
    'pluck':   pluck,                                 
    'spark':   spark,                                 
    'blip':    blip,                                
    'ripple':  ripple,                                 
    'creep':   creep,                                 
    'orient':  orient,                                 
    'zap':     zap,                                 
    'marimba': marimba,                                 
    'fuzz':    fuzz,                                 
    'bug':     bug,                                 
    'pulse':   pulse,                                 
    'saw':     saw,                                 
    'snick':   snick,                               
    'twang':   twang,                                 
    'karp':    karp,                                 
    'arpy':    arpy,                                 
    'nylon':   nylon,                                 
    'donk':    donk,                                 
    'squish':  squish,                                 
    'swell':   swell,                                 
    'razz':    razz,                                 
    'sitar':   sitar,                                 
    'star':    star,                               
    'jbass':   jbass,                                 
    'piano':   piano,                                 
    'sawbass': sawbass,                                 
    'prophet': prophet,                                 
    'pads':    pads,                                 
    'pasha':   pasha,                                 
    'ambi':    ambi,                                 
    'space':   space,                                 
    'keys':    keys,                                 
    'dbass':   dbass,                               
    'sinepad': sinepad,                               
    }

test_def = {'prophet': prophet, 'pads': pads, 'pasha': pasha}


def use_synth_def(action):
    return getattr(action)


def runit(synth_item):
    # for synth_x in synth_defs.items():
    # p1 >> synth_defs['noise']([0, 2, 4, 5, 7, 9, 10])
    # p1 >> synth_defs['noise']([0, 2, 4, 5, 7, 9, 10]).stop(4)
    p2 >> synth_defs['dab']([0, 2, 4, 5, 7, 9, 10])
    # p2 >> synth_defs['dab']([0, 2, 4, 5, 7, 9, 10]).stop(4)

    # p1 >> synth_defs[synth_x[0]]([0, 2, 4, 5, 7, 9, 10]).stop(4)
    # p1 >> synth_defs[synth_item]([0, 1, 2, 3])
    # p1 >> pads([0, 1, 2, 3])
    # p1 >> play("x-o-")
    #     p1 >> blip().stop(8)
    Go()

if __name__ == "__main__":
    d = iter(synth_defs)
    try:
        while True:
            item = next(d)
            # item = next(d)
            runit(item)
            input(f"aktuell: {item} nächster? -> return")
    except StopIteration:
        print("letzte Synthdef wurde erreicht! Ende!")
        pass