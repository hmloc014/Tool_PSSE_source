import os
import sys
import contextlib

@contextlib.contextmanager
def redirect_stdout(target):
    original = sys.stdout
    try:
        sys.stdout = target
        yield
    finally:
        sys.stdout = original

stdout_fd = sys.stdout.fileno()
with open('output.txt', 'w') as f, redirect_stdout(f):
    print('redirected to a file')
    os.write(stdout_fd, b'not redirected')
    os.system('echo this also is not redirected')