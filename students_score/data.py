# @file: data.py
import random
from collections import namedtuple
Student = namedtuple('Student',['id', 'ans'])
N_QUESTIONS = 20
N_STUDENTS = 25
def gen_random_list(opts, n):
    return [random.choice(opts) for i in range(n)]
# 问题答案“ABCD”随机
ANS = gen_random_list('ABCD',N_QUESTIONS)
# 问题分值1~5分随机
SCORE = gen_random_list(range(1,6), N_QUESTIONS)
quize = list(zip(ANS, SCORE))
students = [
    # 学生答案为'ABCD'随机，* 代表未作答
    Student(_id, gen_random_list('ABCD*', N_QUESTIONS))
    for _id in range(1, N_STUDENTS+1)
]

#print(list(quize))

#print(students)

