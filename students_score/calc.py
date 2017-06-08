from data import students, quize
from functools import reduce
import re
def calc(_quize):
    def inner(_student):
        ziped = zip(_student.ans, _quize)
        filtered = filter(lambda x: x[0] == x[1][0], ziped)
        reduced = reduce(lambda x, y: x + y[1][1], filtered, 0)
        print(_student.id, '\t', reduced)
    return inner

ll = map(calc(quize), students)
for each in ll:
    each

pattern = re.compile(r'hello')