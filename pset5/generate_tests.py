#generate_tests.py -- python 2.7

import random

random.seed(124)

ns = [12, 15, 17, 12, 18, 34]
qs = [11, 7,  35, 6 , 3 , 29]

assert (len(ns) == len(qs))

for i in range(len(ns)):
    filename = "t" + str(i) + ".txt"
    f = open(filename, "w+")


    booths = [random.randint(1, 20) for j in range(ns[i])]
    boothstr = " ".join(str(x) for x in booths)

    queries = [random.randint(1, 20) for k in range(qs[i])]
    qstr = " ".join(str(x) for x in queries)

    f.write(str(ns[i]) + " " + str(qs[i]))
    f.write("\n")
    f.write(boothstr)
    f.write("\n")
    f.write(qstr)

    f.close()
    