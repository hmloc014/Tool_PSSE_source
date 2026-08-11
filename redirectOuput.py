# silence.py
import sys
import os
import pssepath
pssepath.add_pssepath()    
import psspy
import redirect
redirect.psse2py()

import contextlib
@contextlib.contextmanager
def silence(new_target):
    # sometimes you don't care about messages.
    if new_target is None:
        new_target = open(os.devnull, 'w')
    old_target, sys.stdout = sys.stdout, new_target # replace sys.stdout
    try:
        yield new_target # run some code with the replaced stdout
    finally:
        sys.stdout = old_target # restore to the previous value
