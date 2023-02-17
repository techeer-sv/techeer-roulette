import sys
import secrets
from time import sleep

candidates_filename = 'candidates.txt'

if len(sys.argv) > 1:
    candidates_filename = sys.argv[1]

def dot_every(sec, times):
    for _ in range(times):
        dot_and_wait(sec)

def dot_and_wait(sec):
    print('.', end='', flush=True)
    sleep(sec)

try:
    with open(candidates_filename) as f:
        candidates = [line.rstrip('\n') for line in f]

        print('[발표자 명단 - 총원 {}명]'.format(len(candidates)))
        print(str(', '.join(candidates)))
        print()

        sleep(3)

        print('발표자는', end='', flush=True)
        dot_every(0.5, 10)
        print()
        print()

        rand = secrets.randbelow(len(candidates))
        print('"{}"님 입니다!'.format(candidates[rand]))
except FileNotFoundError:
    print('Candidates file specified not found: {}'.format(candidates_filename))
    sys.exit(1)
