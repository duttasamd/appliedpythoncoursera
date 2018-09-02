import datetime as dt
import time as tm

tm.time()
dt.datetime.fromtimestamp(tm.time())

def times_tables():
    lst = []
    # for i in range(10):
    #     for j in range (10):
    #         lst.append(i*j)
    # return lst
    lst = [i*j for i in range(10) for j in range(10) if True]
    return lst 

times_tables()

# --------------------------------------------------

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [ch1 + ch2 + num1 + num2 for ch1 in lowercase for ch2 in lowercase for num1 in digits for num2 in digits]
answer[:50]