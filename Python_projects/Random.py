import random as rd
o = [rd.randint(0, 100) for i in range(100000)] + [rd.choice(['a', 'b', 'c', 'd', 'e']) for i in range(50000)]
rd.shuffle(o)

print(set(o))