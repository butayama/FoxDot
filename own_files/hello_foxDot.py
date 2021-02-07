# hello_FoxDot.py
# example from readme.md

from FoxDot import *

SYNTH_DEFS = ['loop', 'stretch', 'play1', 'play2', 'audioin', 'noise', 'dab', 'varsaw', 'lazer', 'growl',
              'bass', 'dirt', 'crunch', 'rave', 'scatter', 'charm', 'bell', 'gong', 'soprano', 'dub',
              'viola', 'scratch', 'klank', 'feel', 'glass', 'soft', 'quin', 'pluck', 'spark', 'blip',
              'ripple', 'creep', 'orient', 'zap', 'marimba', 'fuzz', 'bug', 'pulse', 'saw', 'snick',
              'twang', 'karp', 'arpy', 'nylon', 'donk', 'squish', 'swell', 'razz', 'sitar', 'star',
              'jbass', 'piano', 'sawbass', 'prophet', 'pads', 'pasha', 'ambi', 'space', 'keys', 'dbass',
              'sinepad']


def use_synth_def(self, action):
    self.synth(getattr(self, action))


def runit():
    p1 >> use_synth_def(SYNTH_DEFS[54]([0, 1, 2, 3]))
    # p1 >> pads([0, 1, 2, 3])
    d1 >> play("x-o-")
    Go()

if __name__ == "__main__":
    runit()