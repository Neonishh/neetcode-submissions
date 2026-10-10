from typing import List

def read_integers() -> List[int]:
    a = input().split(",")
    return [int(x) for x in a]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
