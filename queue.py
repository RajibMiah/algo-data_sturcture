
from collections import deque



if __name__ == "__main__":
    q = deque()
    q.appendleft(5)
    q.appendleft(10)
    q.appendleft(8)

    print(q.pop())