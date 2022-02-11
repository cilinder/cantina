from inspect import EndOfBlock
import random as rnd

for i in range(100):
    n = rnd.randrange(4,1000)
    k = rnd.randrange(2,100)

    with open(f'examples/example_{i}.txt', 'w', encoding='utf-8') as file:
        file.write(str(n)+"\n")
        for i in range(n):
            r = rnd.randrange(1, k+1)
            languages = rnd.sample(range(k), r)
            file.write(str(i))
            for l in languages:
                file.write(" " + str(l))
            file.write("\n")
