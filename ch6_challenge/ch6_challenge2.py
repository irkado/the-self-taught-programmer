import random
import statistics
from ch6_challenge1 import cubed

if __name__ == "__main__":
    list1 = [random.randint(0, 100) for i in range(1, 10)]  # i
    list2 = [random.randint(0, 100) for i in range(1, 10)]  # j

    mt = [[i * j for j in list2] for i in list1]

    print("\n    " + "   ".join(f"{x}" for i, x in enumerate(list2)))  # j
    print("\n".join(f"{list1[i]} - {x}" for i, x in enumerate(mt)))

    median = statistics.mode([int(statistics.mode(el)) for el in mt])
    print(median)

    [print("\n".join(f"-{i}-" for i in elem if i == median)) for elem in mt]

    print("\n", cubed(int(median)))
    
    # matrix = [[i * j for j in range(5)] for i in range(5)]
    # print("    0  1  2  3  4  5")
    # print('\n'.join(f'{i} - {x}' for i,x in enumerate( matrix)))
