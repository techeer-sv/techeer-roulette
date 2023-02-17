import sys
from random import shuffle
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

        shuffle(candidates)

        input('Enter를 눌러 진행하세요.')
        print()

        for i in range(len(candidates)):
            print('다음 발표자는...', end='', flush=True)
            input()
            print('"{}"님 입니다!'.format(candidates[i]))
            print()
except FileNotFoundError:
    print('Candidates file specified not found: {}'.format(candidates_filename))
    sys.exit(1)
